import os, re, sys, glob, json, hashlib

DOCS_DIR = "content/docs"
LOTO_DIR = os.path.join(DOCS_DIR, "02-loto-standards")
errors = []

def read(p):
	with open(p, encoding="utf-8") as f:
		return f.read()

# 1. Mọi thư mục trong content/docs phải có _index.md (giữ nguyên kiểm tra gốc)
missing = []
for root, dirs, files in os.walk(DOCS_DIR):
	if "_index.md" not in files:
		missing.append(root)
if missing:
	errors.append("THIẾU FILE _index.md TẠI CÁC THƯ MỤC SAU:\n" + "\n".join(" - " + m for m in missing))

# 2. Mã SHA-256 của từng SOP LOTO: tính lại từ payload và đối chiếu với mọi nơi được trích dẫn
index_pages = [os.path.join(LOTO_DIR, "loto-sop-sha256-v3.md"), os.path.join("content", "_index.md")]
index_text = {p: read(p) for p in index_pages if os.path.exists(p)}
for f in sorted(glob.glob(os.path.join(LOTO_DIR, "loto-elec-*.md"))):
	t = read(f)
	sop = re.search(r'^sop_id:\s*"([^"]+)"', t, re.M).group(1)
	front = re.search(r'^sha256_checksum:\s*"([0-9a-f]{64})"', t, re.M).group(1)
	m = re.search(r'payload_data = (\{.*?\n\})\n\n# Re-compute', t, re.S)
	payload = json.loads(re.sub(r'\bTrue\b', 'true', re.sub(r'\bFalse\b', 'false', re.sub(r'\bNone\b', 'null', m.group(1)))))
	real = hashlib.sha256(json.dumps(payload, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()
	if real != front:
		errors.append("%s: hash tính lại %s khác front matter %s" % (sop, real, front))
	for p, txt in index_text.items():
		for h in re.findall(re.escape(sop) + r'[^\n]*?`([0-9a-f]{64})`', txt):
			if h != real:
				errors.append("%s: %s ghi hash sai %s (đúng: %s)" % (sop, p, h, real))

# 3. Cú pháp đã deprecated và link tuyệt đối trỏ về chính site (phải dùng relref)
for p in glob.glob("content/**/*.md", recursive=True):
	t = read(p)
	if re.search(r'\{\{[<%]\s*hint\b', t):
		errors.append("%s: dùng shortcode hint (deprecated), đổi sang > [!NOTE]" % p)
	if re.search(r'\{\{<\s*katex\s+display=', t):
		errors.append("%s: katex display= (deprecated), đổi sang displayMode=" % p)
	if re.search(r'\]\(https://nguyentridung-ot\.github\.io/ot-tech-blog/', t):
		errors.append("%s: link tuyệt đối tới chính site, hãy dùng relref" % p)

if errors:
	print("❌ PHÁT HIỆN LỖI:")
	for e in errors: print(" - " + e)
	sys.exit(1)
print("✅ CẤU TRÚC THƯ MỤC, SHA-256 VÀ CÚ PHÁP ĐỀU HỢP LỆ!")
