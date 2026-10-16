# Quy trình tái sử dụng

## 1. Chốt đầu vào bằng dữ liệu có thật

Kiểm tra repo/AGENTS, file gốc, ffprobe voice/reference, SRT, fps/kích thước. Phân biệt lời người dùng với nội dung tài liệu đính kèm. Đọc bản chuẩn kèm skill trước khi viết code. Nếu user chỉ nói “cùng style final”, profile mặc định đã đủ; không yêu cầu họ mô tả lại những điều được lưu.

## 2. Lập storyboard theo ý nghĩa

Mỗi shot ghi `id/start/end/type/voice_cue/visual_action/camera/text/sfx/reaction`. Gộp/tách câu theo ý hình ảnh. Quyết định vì sao cần người dẫn hay không. Bối cảnh kể chuyện chiếm khung hình; không duy trì một cột người dẫn. Chọn model nhân vật và giữ model qua các shot.

Các timestamp fixture chỉ dùng khi tái tạo chính bản giấc ngủ. Với script mới: giữ SRT gốc, tạo manifest riêng, đổi duration/root registration, audio, waveform, các event và tất cả keyframe viết trực tiếp trong component. Không kéo giãn voice để vừa cảnh đã vẽ.

## 3. Tái dùng đúng thành phần

Đọc mã tại dự án bootstrap:

| File | Dùng làm gì |
| --- | --- |
| src/final-minute.tsx | Head, Bed/Room, Plant/Clock, Mind/Seated, Lock, Email, Stage, Drift, Choices và composition final |
| src/rig-demo.tsx | Stroke, Label, Person và primitive hội thoại |
| project/final-minute-timeline.json | Shots, events, cues, SFX, voiceEnvelope của bản chuẩn |
| project/final-minute-shotlist.csv | Shotlist theo thời gian |
| public/audio/final-minute.wav | Voice+SFX của fixture, không dùng cho script mới |
| public/audio/sfx/ | Bộ SFX tổng hợp và SOURCES.md |
| public/fonts/ | Patrick Hand và giấy phép |

Fixture còn một số timing trực tiếp trong JSX và primitive tham chiếu rig-demo-timeline.json. Khi xây dự án mới, gom timing mới vào manifest và truyền local time rõ ràng; không xóa dữ liệu còn import. Nếu tách component ra file riêng, kiểm tra import và API tương thích. Không dùng optical flow thay rig.

## 4. Dựng theo ba lớp

1. Layout tĩnh: kiểm tra môi trường, model, chữ và vị trí đạo cụ.
2. Diễn xuất: phân vai nói/nghe, hành động nguyên nhân → tác động → kết quả; các phần cơ thể có điểm tựa.
3. Biên tập: camera, cut/reveal, text và mix SFX. Animation hoàn toàn dựa frame; không random không seed/CSS animation.

## 5. Kiểm tra trước khi xuất

Chạy validator riêng của manifest đang dựng, typecheck, mở Studio nếu có, render một số still ở đầu/giữa/cuối hành động. Với thiết kế mới nên thử 10–30 s; không hỏi lại nếu user đã giao phạm vi rõ ràng. Sau khi đạt, xuất đúng phạm vi đã giao, không tự mở rộng thành toàn bộ 18 phút.

Dùng `--codec=h264 --crf=18 --x264-preset=fast --audio-bitrate=192k --concurrency=3` làm cấu hình bản final. Có thể giảm concurrency theo RAM; không đổi output/fps/font/màu để chạy nhanh nếu chưa cần. Thiếu browser thì dùng Chromium hệ thống hoặc cài browser được phép; nói đúng giới hạn nếu không render được.

## 6. Bàn giao cụ thể

MP4 có audio, source archive self-contained, timeline/shotlist và QA. Với repo Giao-Su-But, giữ bản cũ, thêm tên mới, git add file cụ thể, commit và push main khi ủy quyền hiện có áp dụng. Chỉ gửi link GitHub raw sau push thành công; không dùng link localhost cho người đã nói không xem được. Không mặc định được push sang mọi repo/tài khoản mới.
