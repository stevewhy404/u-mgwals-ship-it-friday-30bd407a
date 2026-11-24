import os

LINE = "feat: deleted every test and shipped to prod at 4:59pm, it's Friday, what could possibly go wrong?"

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
