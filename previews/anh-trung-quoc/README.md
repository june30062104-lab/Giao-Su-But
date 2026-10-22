# Cách mạng công nghiệp: Anh và Trung Quốc — bản thử đầu tiên

[Tải MP4 — 26,8 giây, 1080p](https://github.com/june30062104-lab/Giao-Su-But/raw/refs/heads/main/previews/anh-trung-quoc/ban-thu-27s.mp4)

[Tải source và tài nguyên](https://github.com/june30062104-lab/Giao-Su-But/raw/refs/heads/main/sources/anh-trung-quoc-ban-thu-source.zip) · [Contact sheet](contact.jpg).

## Phạm vi

Người dùng cung cấp bộ prompt, voice MP3 và SRT mới. Đã chuyển 116 cảnh thành dữ liệu và đối chiếu các mốc với toàn bộ 204 câu SRT. Voice dài 899,78775 giây; câu SRT cuối kết thúc ở 899,640 giây.

Bản thử chỉ dựng 3 cảnh đầu (001–003), từ đầu đến 26,8 giây, kết thúc trọn câu ở 26,520 giây. Chưa render toàn bộ video gần 15 phút.

- Toàn cảnh lò luyện sắt thời Tống: người tiếp quặng, rót kim loại vào khuôn, viên quan giám sát; lửa và một số hiệu ứng chuyển động riêng.
- Cận than đá làm nhiên liệu.
- Sổ thuế và con số có thể vượt 100.000 tấn/năm, ghi rõ tính ước tính.
- Học giả đối chiếu tư liệu: số thuế không đồng nghĩa sản lượng thực tế; giữ sự bất định như voice.

Bối cảnh tạo mới bằng công cụ tạo ảnh; nhân vật và đạo cụ SVG tách khỏi nền, có thay đổi mắt/đầu/tay/gầu và hiệu ứng rót/lửa. Nhân vật đầu tròn trắng, tay chân mảnh, màu phẳng ấm, font Patrick Hand. Không lấy hình lịch sử này làm phục dựng khảo cổ được xác minh từng chi tiết.

Voice gốc giữ nguyên tốc độ, gain 0,9; có SFX tổng hợp và ambience nhẹ. Không thay bằng TTS, không thêm nhạc nền.

## QA

TypeScript và kiểm dữ liệu đạt. Tất cả 116 cảnh có timestamp khớp SRT được cung cấp (không có nghĩa đã thẩm định tính chính xác lịch sử của lời thoại). Bản thử có 4 shot liên tục, 804 frame, 1920×1080/30 FPS, H.264/AAC; container 26,816 giây. Giải mã toàn bộ không báo lỗi; đã kiểm contact sheet toàn đoạn và khung hình rót kim loại, học giả. Mix peak trước encode 0,532, không clipping.
