import os, sys
DOCS_DIR = "content/docs"
missing = []
for root, dirs, files in os.walk(DOCS_DIR):
	if "_index.md" not in files:
		missing.append(root)
if missing:
	print("❌ THIẾU FILE _index.md TẠI CÁC THƯ MỤC SAU:")
	for m in missing: print(" - " + m)
	sys.exit(1)
print("✅ CẤU TRÚC THƯ MỤC HOÀN HẢO!")