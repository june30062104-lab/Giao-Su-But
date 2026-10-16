# Bản chuẩn có thể chạy lại

- Style ID: `sleep-final-1m-v1`.
- Video đã giao: [MP4](https://github.com/june30062104-lab/Giao-Su-But/raw/refs/heads/main/previews/giac-ngu-final-1-phut.mp4).
- [Contact sheet](https://github.com/june30062104-lab/Giao-Su-But/blob/main/previews/giac-ngu-final-1-phut-contact.jpg).
- Commit tạo video: `5abb6eb`.
- Dự án gốc: assets/final-minute-project.zip, SHA-256 trong assets/profile.json. Có font, mix, SFX và source; không phụ thuộc đường dẫn workspace cũ hoặc tệp Sediment.
- 62,4 giây, 1.872 frame, 1080p30, H.264/AAC; 18 shot; 32 placement / 31 SFX. Giữ voice gốc ở tốc độ ban đầu.

## Chạy lại

```bash
python /path/to/skill/scripts/check_bundle.py
python /path/to/skill/scripts/bootstrap.py /workspace/sleep-replay
cd /workspace/sleep-replay
npm install
npm run typecheck
npx --no-install remotion render src/index.ts SleepFinalMinute output.mp4 --codec=h264 --crf=18 --x264-preset=fast --audio-bitrate=192k --concurrency=3 --browser-executable=/usr/bin/chromium
npm run qa
```

bootstrap kiểm hash và chỉ giải nén vào thư mục mới/rỗng. Không chép đè dự án đang làm. Dependencies trong package.json của fixture được pin version chính xác. Trên máy không có đường dẫn Chromium ở trên, bỏ flag hoặc chọn browser phù hợp. Giữ seed, timing, font và SVG để tái tạo hình ảnh. Trường hợp cần so ảnh, dùng đúng frame của fixture: room 210, kéo chăn 800, stage 1020, dawn 1410, dialogue 1810.

Không hứa MP4 render lại có SHA giống MP4 gốc: codec/browser/OS có thể làm file khác byte. Nếu yêu cầu cùng file, tải file MP4 đã giao rồi kiểm hash. Nội dung fixture là bản final theo người dùng chọn làm chuẩn cho lần sau; không tuyên bố đã đạt kiểm duyệt thẩm mỹ độc lập.

## Phạm vi tham chiếu đã xem

Bản tham khảo truy cập được là `1016 (3).mp4`, 71,63356 s, 854×480/30 FPS; đã xem lại overview và đoạn 00:54. Tệp `source .mp4` gửi sau đó vượt giới hạn tải 32 MiB nên chưa mở. Lần sau chuẩn trực tiếp là **video final trong repo**, không yêu cầu tải lại tệp mẫu lớn để bắt đầu.
