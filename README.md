<!-- README for pdf_xml_checker -->

# pdf_xml_checker

Lightweight utility to detect and attempt to repair corrupted PDF and XML files.

[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Summary

- Check PDF header and EOF markers for structural issues
- Try opening and repairing PDFs using `pikepdf` (when available)
- Validate and recover XML using `lxml`

Quick start

1. Install runtime dependencies:

```bash
python -m pip install -r requirements.txt
```

<!-- README for pdf_xml_checker -->

# pdf_xml_checker

Lightweight utility to detect and attempt to repair corrupted PDF and XML files.

[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

What it does

- Checks PDF header and EOF markers for structural issues
- Attempts to open and repair PDFs using `pikepdf` (if available)
- Validates and recovers XML using `lxml`

Quick start

1. Install runtime dependencies:

```bash
python -m pip install -r requirements.txt
```

2. Run the CLI:

```bash
python cli.py check-pdf samples/file.pdf
python cli.py repair-pdf samples/corrupt.pdf repaired.pdf
python cli.py check-xml samples/file.xml
python cli.py repair-xml samples/corrupt_file.xml repaired.xml
```

Optional: install locally

```bash
python -m pip install -e .
# then run: pdf-xml-checker check-pdf samples/file.pdf
```

Notes on native dependencies

- `pikepdf` requires the `qpdf` native library. If you run repair features inside containers or AWS Lambda, include `qpdf` in the image or layer.
- `lxml` typically provides wheels for common platforms; if building from source ensure `libxml2`/`libxslt` are available.

Security

- Treat uploaded/untrusted files cautiously. For production, run processing in isolated environments.

Contributing

- Bug reports and PRs welcome. Open issues and target the `main` branch.

License

- MIT — see the `LICENSE` file.
