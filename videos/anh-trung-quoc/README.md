# Cách mạng công nghiệp: Anh và Trung Quốc — bản đầy đủ

**[Tải video đầy đủ — MP4 1080p, khoảng101MB](https://github.com/june30062104-lab/Giao-Su-But/raw/refs/heads/main/videos/anh-trung-quoc-full-1080p.mp4)**

15 phút · 1920×1080 · 16:9 · 30 FPS · H.264/AAC · 27000khung hình.

- [Tải SRT gốc](https://github.com/june30062104-lab/Giao-Su-But/raw/refs/heads/main/videos/anh-trung-quoc-full.srt).
- [Tải source, voice và tài nguyên — ZIP khoảng72MB](https://github.com/june30062104-lab/Giao-Su-But/raw/refs/heads/main/sources/anh-trung-quoc-full-project.zip).
- [Xem contact sheet toàn video](contact.jpg) · [Shotlist116cảnh](shotlist.csv) · [QA đo được](qa-report.json).

## Nội dung và cách dựng

Triển khai toàn bộ116cảnh từ bộ prompt và204câu SRT người dùng cung cấp. Voice giữ nguyên tốc độ, trộn SFX/ambience bên dưới. Có223event SFX từ31file được dùng, không thêm nhạc hoặc TTS thay voice.

Giữ nét vẽ tay, nền giấy kem, màu phẳng ấm và nhân vật đầu trắng/tay chân mảnh theo bản thử đã duyệt. 29nhóm cách thể hiện: cảnh kể chuyện trong bối cảnh, nhân vật hành động, cận vật thể, máy hơi nước, xưởng dệt, giao thương, thí nghiệm/trao đổi, ngoại giao, sơ đồ, dữ liệu, đường sắt và công nghiệp hiện đại.12bối cảnh được tạo mới rồi kết hợp với nhân vật/máy móc/đạo cụ SVG riêng; không phải116ảnh AI độc lập, không để người dẫn cạnh bảng xuyên suốt.

Các con số và sự bất định được giữ theo kịch bản: ước tính sắt thời Tống không so trực tiếp với số liệu gang thô Anh; GDP là tỷ trọng ước tính lịch sử. Tính đúng của timestamp đã được đối chiếu với SRT; đó không phải lời khẳng định đã fact-check độc lập toàn bộ số liệu lịch sử/hiện đại. Bản đồ và cơ chế máy là sơ đồ minh họa, không phải bản đồ ranh giới hay bản vẽ kỹ thuật đo đạc chính xác.

## Các chương trong MP4

| Mốc | Nội dung |
| --- | --- |
| 00:00 | Lò luyện sắt và câu hỏi công nghiệp hóa |
| 01:17 | Thành tựu kỹ thuật và kinh tế Trung Quốc |
| 02:59 | Mỏ than, nước ngầm và động cơ hơi nước |
| 04:44 | Địa lý tài nguyên và vận tải |
| 05:40 | Tiền công, năng lượng và cơ giới hóa |
| 06:48 | Thương mại, nguyên liệu và bóc lột |
| 08:11 | Khoa học, kỹ thuật và kinh doanh |
| 09:43 | Chính trị và ngoại giao |
| 11:18 | Những ngành sản xuất hỗ trợ nhau |
| 12:24 | Sức mạnh công nghiệp và thế kỷXIX |
| 13:31 | Công nghiệp hóa Trung Quốc hiện đại |
| 14:10 | Điều kiện để phát minh phát triển |

## Kiểm tra bàn giao

- Đủ116cảnh liên tục và204câu SRT; nguồn đầu vào giữ nguyên.
- MP4 đo được900,000giây, 27000frame, 1080p/30FPS, H.264/AAC;12chương.
- Giải mã toàn bộ không báo lỗi. Kiểm âm thanh qua ba điểm nối ở145/445/745giây, tương quan với mix gốc từ0,9989 đến0,9995.
- Mix peak trước AAC0,82945, không clipping. Bản bàn giaoAAC96k mono được mã hóa trực tiếp từ WAV mix; hình được giữ nguyên bitstream của master khi ghép chương, không encode lại để giảm dung lượng.
- Đã rà khung hình đại diện của116cảnh và khung hình thực của MP4; sửa bối cảnh đồng quê Anh, đồn điền châu Mỹ và vị trí đạo cụ ở cảnh kết.
- Source đóng gói mix FLAC lossless (đã xác nhận giải mã trùng mẫuPCM), có lệnh khôi phụcWAV và hai đường xuất: Remotion/Chromium hoặc raster cùng React SVG bằngFFmpeg/librsvg. Miệng chuyển theo biên độ, chưa phải lip-sync âm vị.
