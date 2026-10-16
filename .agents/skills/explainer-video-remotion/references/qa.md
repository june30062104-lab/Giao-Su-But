# QA trước bàn giao

## Kỹ thuật

- Validator đúng composition: liên tục từ 0 đến duration; không thiếu audio/asset; cue/event trong khoảng; frame count đúng FPS; envelope đủ frame. Không lấy `npm run check` của full video 18 phút làm bằng chứng cho một composition mới.
- TypeScript đạt; font tiếng Việt không rơi về fallback; media được load trước frame cần xuất hiện.
- ffprobe: H.264/AAC, đúng kích thước/fps/duration/frame count. Decode toàn clip bằng ffmpeg không lỗi. Kiểm clipping/loudness, voice nguyên tốc độ, đầu/cuối không cắt câu/SFX.
- Fixture: chạy `npm run qa` (scripts/qa-final-minute.py). Composition mới: `python /path/to/skill/scripts/validate_project.py /path/to/project/project/new-timeline.json --public /path/to/project/public`, rồi ffprobe/decode output tương ứng.
- Có thể dùng freezedetect 3 s để tìm đoạn cần xem; đó là kiểm kỹ thuật. Có chuyển động pixel không có nghĩa cảnh có diễn xuất tốt. Fade đen chủ đích không phải lỗi.

## Thẩm mỹ — phải xem khung hình/chuỗi hành động

- Có lặp bố cục người dẫn + bảng không? Nhân vật nói chỉ xuất hiện khi có vai trò?
- Mỗi ý có cách thể hiện phù hợp? Cảnh thực có toàn/cận và phối cảnh, không chỉ icon?
- Trong mọi khoảng 3 s, có hoạt động có ý nghĩa? Không dùng rung/zoom vô cớ để vượt kiểm tra.
- Chân không trượt; người nói/nghe lệch pha; miệng đóng khi im; không chớp mắt máy móc cùng lúc.
- Chuỗi tay: trước khi nắm, tại điểm nắm, giữa khi kéo, kết thúc. Tay gắn với vật, nếp vải/vật thay đổi đúng; không tay kép, xuyên vật hoặc chữ che tay.
- Model nhân vật và màu nhất quán theo vai; text đọc được, không đè mắt/đạo cụ, không dư chữ trong lúc cần nhìn hành động.
- SFX không át voice, không một pop lặp mãi; thông tin mới có âm nhấn khi hợp lý.
- Rà contact sheet toàn clip và 2–4 frame/giây ở hành động khó; contact sheet không thay việc xem chuyển động/kiểm âm thanh khi có công cụ.

## Báo cáo chính xác

Chỉ ghi những kiểm tra thật đã chạy. Tách thông số đo được khỏi nhận xét. Ghi giới hạn chưa nghe/xem được hoặc chưa lip-sync âm vị. Lưu MP4 cũ; đặt tên revision mới khi sửa; không gọi một source chưa render là video hoàn tất.
