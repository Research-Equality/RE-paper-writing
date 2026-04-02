#!/usr/bin/env python3
"""
Convert literature and project documents to Markdown for downstream writing.

Requires the external `markitdown` package:
  pip install 'markitdown[pdf,docx,pptx,xlsx]'
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

from markitdown import MarkItDown


SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".pptx",
    ".xlsx",
    ".xls",
    ".csv",
    ".html",
    ".xml",
    ".json",
}


def extract_metadata_from_filename(filename: str) -> Dict[str, str]:
    metadata: Dict[str, str] = {}
    stem = Path(filename).stem

    year_match = re.search(r"\b(19|20)\d{2}\b", stem)
    if year_match:
        metadata["year"] = year_match.group()

    parts = re.split(r"[_\-]", stem)
    if len(parts) >= 2:
        metadata["author"] = parts[0].replace("_", " ").strip()
        metadata["title"] = " ".join(parts[1:]).replace("_", " ").strip()
    else:
        metadata["title"] = stem.replace("_", " ").strip()

    return metadata


def iter_input_files(input_dir: Path, recursive: bool) -> Iterable[Path]:
    pattern = "**/*" if recursive else "*"
    for path in sorted(input_dir.glob(pattern)):
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS:
            yield path


def build_output_path(output_dir: Path, source: Path, metadata: Dict[str, str], organize_by_year: bool) -> Path:
    if organize_by_year and metadata.get("year"):
        target_dir = output_dir / metadata["year"]
    else:
        target_dir = output_dir
    target_dir.mkdir(parents=True, exist_ok=True)
    return target_dir / f"{source.stem}.md"


def convert_one(md: MarkItDown, source: Path, output_dir: Path, organize_by_year: bool) -> Tuple[bool, Dict[str, str]]:
    metadata = extract_metadata_from_filename(source.name)
    metadata["source_file"] = source.name
    metadata["source_path"] = str(source)
    metadata["converted"] = datetime.now().isoformat(timespec="seconds")

    try:
        result = md.convert(str(source))
        if result.title and not metadata.get("title"):
            metadata["title"] = result.title

        output_path = build_output_path(output_dir, source, metadata, organize_by_year)
        title = metadata.get("title", source.stem)

        lines = [
            "---",
            f'title: "{title}"',
            f'source_file: "{metadata["source_file"]}"',
            f'source_path: "{metadata["source_path"]}"',
            f'converted: "{metadata["converted"]}"',
        ]
        if metadata.get("author"):
            lines.append(f'author: "{metadata["author"]}"')
        if metadata.get("year"):
            lines.append(f'year: "{metadata["year"]}"')
        lines.extend(["---", "", f"# {title}", ""])
        if metadata.get("author"):
            lines.append(f'**Author**: {metadata["author"]}')
        if metadata.get("year"):
            lines.append(f'**Year**: {metadata["year"]}')
        lines.extend(
            [
                f'**Source File**: {metadata["source_file"]}',
                f'**Converted**: {metadata["converted"]}',
                "",
                "---",
                "",
                result.text_content,
            ]
        )

        output_path.write_text("\n".join(lines), encoding="utf-8")
        metadata["output_markdown"] = str(output_path)
        return True, metadata
    except Exception as exc:  # pragma: no cover - best effort wrapper
        metadata["error"] = str(exc)
        return False, metadata


def create_index(records: List[Dict[str, str]], output_dir: Path) -> None:
    records = sorted(records, key=lambda item: (item.get("year", "9999"), item.get("title", "")))

    index_lines = [
        "# Source Material Index",
        "",
        f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"**Total Converted Files**: {len(records)}",
        "",
        "---",
        "",
    ]

    for record in records:
        title = record.get("title", record.get("source_file", "unknown"))
        output_markdown = record.get("output_markdown", "")
        index_lines.append(f"## {title}")
        if record.get("author"):
            index_lines.append(f"- Author: {record['author']}")
        if record.get("year"):
            index_lines.append(f"- Year: {record['year']}")
        index_lines.append(f"- Source: {record.get('source_file', 'unknown')}")
        if output_markdown:
            rel = Path(output_markdown).relative_to(output_dir)
            index_lines.append(f"- Markdown: [{rel}]({rel})")
        if record.get("error"):
            index_lines.append(f"- Error: {record['error']}")
        index_lines.append("")

    (output_dir / "INDEX.md").write_text("\n".join(index_lines), encoding="utf-8")
    (output_dir / "catalog.json").write_text(json.dumps(records, indent=2, ensure_ascii=False), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert literature and project documents to Markdown.")
    parser.add_argument("input_dir", type=Path, help="Directory containing source files")
    parser.add_argument("output_dir", type=Path, help="Directory for converted Markdown files")
    parser.add_argument("--organize-by-year", "-y", action="store_true", help="Place converted files into year subdirectories")
    parser.add_argument("--recursive", "-r", action="store_true", help="Search subdirectories recursively")
    parser.add_argument("--create-index", "-i", action="store_true", help="Write INDEX.md and catalog.json")
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    md = MarkItDown()

    converted: List[Dict[str, str]] = []
    for source in iter_input_files(args.input_dir, args.recursive):
        success, record = convert_one(md, source, args.output_dir, args.organize_by_year)
        converted.append(record)
        status = "OK" if success else "FAIL"
        print(f"[{status}] {source.name}")

    if args.create_index:
        create_index(converted, args.output_dir)

    total_ok = sum(1 for item in converted if "error" not in item)
    print(f"Converted {total_ok}/{len(converted)} files")


if __name__ == "__main__":
    main()
