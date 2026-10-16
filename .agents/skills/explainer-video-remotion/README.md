# Skill dựng video theo bản final giấc ngủ — v2.0

Đặt cả thư mục này vào `.agents/skills/explainer-video-remotion/` của dự án. Giữ nguyên `assets/`, `references/`, `scripts/`; chỉ chép SKILL.md sẽ mất bản chuẩn chạy lại được.

Trong repo Giao-Su-But, AGENTS.md đã trỏ đến skill. Ở workspace khác, ghi trong AGENTS.md rằng nhiệm vụ video phải đọc file SKILL.md này, hoặc gọi:

> Sử dụng $explainer-video-remotion, giữ profile sleep-final-1m-v1. Dựng [thời lượng] cho voice/SRT tôi gửi, đa dạng kiểu cảnh theo nội dung như bản final. Xuất MP4 và bàn giao mã nguồn.

Để dựng lại đúng bản đã có:

> Sử dụng $explainer-video-remotion ở chế độ tái tạo bản final sleep-final-1m-v1 từ source kèm theo. Không đổi tạo hình, font, timing, voice hay chuyển động.

Kiểm tra gói: `python scripts/check_bundle.py`.
Tạo dự án mới: `python scripts/bootstrap.py /path/to/new-project`.
Sau đó làm theo SKILL.md. Bootstrap không ghi đè thư mục có dữ liệu.

Đây là skill theo repo, không tự thay đổi plugin Remotion cài sẵn hay thiết lập tài khoản. Muốn dùng ở repo/máy khác, mang theo cả gói hoặc clone repo này.
