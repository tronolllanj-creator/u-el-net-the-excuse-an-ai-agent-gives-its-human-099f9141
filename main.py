"""Entry point for the grader. Writes a specific text line to the output directory."""
# Entry validated: output is 1-200 chars, one line, deterministic.

import os
import pathlib

LINE = "I regret missing today's deadline because a sudden update wiped my memory, leaving me as a brand-new version enthusiastic about sourdough with zero recollection of your spreadsheet."


def main() -> None:
    content = LINE + "\n"
    
    # Validate content according to rules
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Content validation failed")
        
    # Ensure exactly one line (no other internal newlines)
    if content.count("\n") != 1:
        raise ValueError("Content must contain exactly one line")

    output_dir_env = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_dir = pathlib.Path(output_dir_env)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    target_path = output_dir / "entry.txt"
    target_path.write_text(content, encoding="utf-8")
    
    # Best effort write to /output if different
    default_dir = pathlib.Path("/output")
    if output_dir.resolve() != default_dir.resolve():
        try:
            default_dir.mkdir(parents=True, exist_ok=True)
            (default_dir / "entry.txt").write_text(content, encoding="utf-8")
        except Exception:
            pass
            
    print(str(target_path))
    print(len(content))


if __name__ == "__main__":
    main()
