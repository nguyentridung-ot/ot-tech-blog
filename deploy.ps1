Write-Host '🚀 Bắt đầu đóng gói và xuất bản Blog lên mạng...' -ForegroundColor Cyan
git add .
git commit -m 'Update blog content'
git push origin main
Write-Host '✅ Đã đẩy code lên GitHub thành công!' -ForegroundColor Green