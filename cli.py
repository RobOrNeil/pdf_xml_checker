import argparse
import json
from pdf_checker import (
    check_pdf_structure,
    can_open_with_pikepdf,
    try_repair_with_pikepdf,
)
from xml_checker import check_xml_wellformed, try_repair_xml


def main():
    # ARGUMENT PARSER
    p = argparse.ArgumentParser(prog="pdf_xml_checker")
    sub = p.add_subparsers(dest="cmd")

    # PDF SUBCoMMAND - CHECK AND REPAIR
    a = sub.add_parser("check-pdf")
    a.add_argument("file")

    b = sub.add_parser("repair-pdf")
    b.add_argument("file")
    b.add_argument("out")

    # XML SUBCOMMAND - CHECK AND REPAIR
    c = sub.add_parser("check-xml")
    c.add_argument("file")

    d = sub.add_parser("repair-xml")
    d.add_argument("file")
    d.add_argument("out")

    # PARSE ARGUMENTS AND EXECUTE
    args = p.parse_args()
    if args.cmd == "check-pdf":
        s = check_pdf_structure(args.file)
        s.update(can_open_with_pikepdf(args.file))
        print(json.dumps(s, indent=2))
    elif args.cmd == "repair-pdf":
        res = try_repair_with_pikepdf(args.file, args.out)
        print(json.dumps(res, indent=2))
    elif args.cmd == "check-xml":
        print(json.dumps(check_xml_wellformed(args.file), indent=2))
    elif args.cmd == "repair-xml":
        print(json.dumps(try_repair_xml(args.file, args.out), indent=2))
    else:
        p.print_help()


if __name__ == "__main__":
    main()
