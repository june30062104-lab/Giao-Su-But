---
name: explainer-video-remotion
description: Dựng video giải thích hoạt hình 2D bằng Remotion theo bản giấc ngủ final 62,4 giây: nét viền tối, màu phẳng ấm, nhân vật tách lớp, nhiều kiểu cảnh theo nội dung, text viết tay và SFX theo voice. Dùng khi người dùng yêu cầu dựng tiếp, tái tạo hoặc áp dụng phong cách bản final giấc ngủ; có dự án chuẩn chạy lại được kèm theo.
---

# Explainer video Remotion — v2.0

Chuẩn mặc định là **sleep-final-1m-v1**, bản final 62,4 giây ở commit `5abb6eb`. Không lấy bản v1/v2 dài, bản minh họa v3 hay bản người dẫn đứng cạnh bảng làm chuẩn. Người dùng yêu cầu giữ cách dựng này cho những lần sau; thay đổi của người dùng luôn ưu tiên hơn các mặc định dưới đây.

## Đọc đúng phần cần dùng

1. Luôn đọc [chuẩn hình ảnh và chuyển động](references/style-and-motion.md).
2. Dựng mới: đọc [quy trình sản xuất](references/production.md) và [QA](references/qa.md).
3. Dựng lại đúng bản final: đọc [bản chuẩn và cách tái tạo](references/golden-master.md); dùng dự án kèm theo, không viết lại bằng phỏng đoán.
4. [profile.json](assets/profile.json) lưu giá trị đo được, hash và cấu hình chuẩn. Các con số của bản 62,4 giây là **fixture**, không áp máy móc cho kịch bản khác.

## Hai chế độ

**Tái tạo bản final:** kiểm tra SHA-256, giải nén bằng `scripts/bootstrap.py` vào thư mục mới, cài dependencies và render composition `SleepFinalMinute`. Giữ nguyên source, timeline, audio, font và model nhân vật. Không tạo lại tài nguyên bằng AI hay đổi font khi đã có bản gốc.

**Nội dung mới cùng phong cách:** sao chép dự án chuẩn làm nền, giữ model/tokens/animation primitives; viết storyboard và timeline mới theo voice/SRT mới. Thay toàn bộ timestamp, envelope âm lượng và âm thanh trộn liên quan. Tìm cả thời gian viết trực tiếp trong JSX; đổi JSON đơn thuần chưa đủ. Không dùng lại email/chăn/phòng ngủ chỉ vì fixture có sẵn khi nội dung không liên quan.

## Các quyết định bắt buộc khi dựng

- Mỗi ý chọn cách thể hiện phù hợp: bối cảnh kể chuyện, nhân vật hành động, cận vật thể, hồi ức, ẩn dụ, sơ đồ hoặc hội thoại. Không mặc định người dẫn bên trái + bảng bên phải. Không cần mọi shot là một kiểu chưa từng dùng; thay đổi có lý do, giữ liên tục không gian khi cần.
- Người dẫn xuất hiện khi giải thích/đặt câu hỏi/đối thoại cần họ. Khi voice kể một hành động, nhân vật **làm hành động đó** trong bối cảnh. Không để người dẫn chỉ tay xuyên suốt.
- Tạo hình cartoon 2D, nét tối, màu phẳng ấm, bóng nhẹ; nền kem cho đoạn trừu tượng. Bối cảnh có phối cảnh/đồ dùng hợp lý. Không tự chuyển sang anime, ảnh thật, bóng đổ 3D hay infographic dạng slide.
- Đầu, mắt, miệng, thân, tay và đạo cụ cần chuyển động độc lập phải được tách trong SVG/layer hoặc có keypose. Khóa model nhân vật theo vai trò. Không dùng pan/zoom ảnh gộp thay cho diễn xuất.
- Không để cảnh chết quá 3 giây: có hành động, phản ứng, thay nét mặt, chuyển động môi trường, reveal có ý nghĩa hoặc đổi góc. Không chữa bằng lắc lư mọi thứ, zoom liên tục hay nhồi chữ/SFX.
- Chuyển động tiết chế: chân giữ tại sàn, hai nhân vật không cùng pha; lắc lư chỉ hợp với đứng/nói, thở hợp với nằm. Tay phải nắm đúng vật, vật chịu tác động và có trạng thái kết thúc.
- Text là overlay ngắn, font Patrick Hand Unicode, highlight viết tay, dấu hỏi/gạch đỏ theo ý. Không chép nguyên voice thành chữ lớn mọi cảnh. Phụ đề đầy đủ là lựa chọn riêng nếu được yêu cầu.
- SFX theo thông tin mới/hành động/chuyển ý có ý nghĩa; đa dạng, nhỏ dưới voice, tránh spam cho từng lần chớp mắt/lắc lư. Giữ tốc độ voice gốc; không tự thêm nhạc hoặc TTS thay voice đã có.
- Mọi chuyển động xác định bằng frame; không CSS animation, không random không seed, không optical-flow giữa hai tranh nếu tạo tay kép/nhòe hình.

## Timing và phạm vi

- Manifest của **composition đang dựng** là nguồn timing duy nhất (fixture: `project/final-minute-timeline.json`); voice/SRT là nguồn lời nói. Bảo toàn nguyên bản. Scene ghi thời gian toàn clip; local time ghi rõ khi dùng.
- Lập shotlist theo ý, không mặc định một câu một cảnh. Cue trong một câu chưa có word timing phải đánh dấu là lựa chọn dựng, không tuyên bố khớp từng từ.
- Mặc định thử 10–30 giây với dự án mới chưa có chuẩn. Nếu người dùng đã yêu cầu một phút/toàn bộ hoặc đã duyệt chuẩn, tiếp tục đúng phạm vi đó; không hỏi duyệt lại chỉ vì quy tắc thử mặc định.
- Nếu tệp mới không mở được, nêu rõ tệp nào đã xem; tiếp tục phần độc lập với tài liệu đã có. Không nói đã xem tệp vượt giới hạn tải.

## Thao tác

```bash
python /path/to/explainer-video-remotion/scripts/bootstrap.py /workspace/sleep-video
cd /workspace/sleep-video
npm install
npm run typecheck
npx --no-install remotion studio src/index.ts --no-open
npx --no-install remotion render src/index.ts SleepFinalMinute output.mp4 --codec=h264 --crf=18 --x264-preset=fast --audio-bitrate=192k --concurrency=3
npm run qa
```

Trên môi trường có Chromium hệ thống, thêm `--browser-executable=/usr/bin/chromium` cho render/still nếu cần. Dùng Remotion skill cài sẵn để tra API hiện hành khi thay code; không đổi version fixture chỉ vì có bản mới. Người dùng đã chọn tải GitHub trong dự án này; khi được yêu cầu xuất hoặc tiếp tục công việc đã có ủy quyền đó, xuất MP4 và push các file cụ thể, không gửi link localhost thay bản tải.

## Bàn giao và giới hạn

Bàn giao MP4, mã nguồn có tài nguyên/font, manifest/shotlist, QA ngắn và link tải thực sự. Chỉ nói đã xuất/push sau khi thành công. Không tự gửi email/tin nhắn hay xuất bản sang tài khoản khác.

Source kèm theo giúp dựng lại cùng hình, bố cục, timing và chuyển động. File MP4 có thể khác byte theo hệ điều hành/Chromium/encoder; khi cần **đúng file đã giao**, dùng MP4 đã lưu và hash chuẩn. Miệng của fixture chạy theo biên độ RMS, chưa phải lip-sync âm vị. Tái dựng cùng phong cách cho kịch bản mới vẫn cần biên tập, không hứa tự động giống tuyệt đối chỉ từ một prompt.
