# Hero / La Mã — toàn bộ video

255 cảnh, 10 chương, 35:48.9, 1920×1080 / 30 fps. Dựng bằng Remotion: nhân vật và đạo cụ tách lớp, có di chuyển đến nơi làm việc, thao tác và vận chuyển. Đoạn mở đầu đã duyệt được giữ nguyên. Voice do người dùng cung cấp, nối phần 1 rồi phần 2, không thay tốc độ; SFX theo hành động, không nhạc nền.

## Tải video

- [Video đầy đủ — một file 1080p](https://github.com/june30062104-lab/Giao-Su-But/raw/refs/heads/main/videos/hero-la-ma-full-1080p.mp4).
- Bản HQ giữ chất lượng hình gốc: [phần 1 — 00:00 đến 18:03.7](https://github.com/june30062104-lab/Giao-Su-But/raw/refs/heads/main/videos/hero-la-ma-HQ-part-1.mp4), [phần 2 — 18:03.7 đến hết](https://github.com/june30062104-lab/Giao-Su-But/raw/refs/heads/main/videos/hero-la-ma-HQ-part-2.mp4).
- [Phụ đề SRT toàn bộ](https://github.com/june30062104-lab/Giao-Su-But/raw/refs/heads/main/videos/hero-la-ma-full.srt).
- [Mã nguồn và tài nguyên](https://github.com/june30062104-lab/Giao-Su-But/raw/refs/heads/main/sources/hero-la-ma-full-source.zip).

Giới hạn 100 MiB/tệp của GitHub khiến bản liền mạch cần nén thêm (cùng độ phân giải và nội dung); hai phần HQ giữ nguyên luồng hình gốc. File source có audio mix lossless FLAC và script phục hồi WAV.

## Chương

| Chương | Bắt đầu | Nội dung |
|---|---|---|
| 01 | 00:00 | MỞ ĐẦU: PHÉP MÀU HƠI NƯỚC |
| 02 | 02:43 | ALEXANDRIA VÀ CÁC KỸ SƯ CỔ ĐẠI |
| 03 | 07:55 | CÔNG NGHỆ CỔ ĐẠI ĐÃ TIẾN ĐẾN ĐÂU? |
| 04 | 13:44 | NGUYÊN NHÂN 1 — LAO ĐỘNG VÀ NÔ LỆ |
| 05 | 17:05 | NGUYÊN NHÂN 2 — NHIÊN LIỆU |
| 06 | 19:51 | NGUYÊN NHÂN 3 — KỸ THUẬT VÀ VẬT LÝ |
| 07 | 23:12 | NGUYÊN NHÂN 4 — MÔI TRƯỜNG TRI THỨC |
| 08 | 26:51 | NGUYÊN NHÂN 5 — TIỀN BẠC VÀ ĐẦU TƯ |
| 09 | 30:03 | TRI THỨC TỒN TẠI VÀ ĐỘNG CƠ NEWCOMEN |
| 10 | 33:50 | TRỞ LẠI NGÔI ĐỀN VÀ CTA |

## Kiểm tra

Xem [QA](qa.json), [ảnh các chương](contact-chapters.jpg) và chuỗi hành động [đi lại](walk-action.jpg), [cần cẩu](crane-action.jpg), [Newcomen](newcomen-action.jpg). Timeline và lời đọc đối chiếu với CSV/SRT 255 cảnh. Các mốc hành động bên trong câu là lựa chọn biên tập, chưa phải căn từng từ hay lip-sync âm vị.

Composition `HeroFull` giữ mở đầu từ renderer Chromium; phần SVG còn lại dùng cùng React scene components, raster bằng FFmpeg/librsvg để xuất bản dài. Source cũng có lệnh render toàn bộ qua Remotion/Chromium. Chi tiết trong FULL-VIDEO.md của source.
