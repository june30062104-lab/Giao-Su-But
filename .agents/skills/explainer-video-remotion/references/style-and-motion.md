# Chuẩn tạo hình, diễn xuất và nhịp dựng

## Hình ảnh đo từ source final

- Output 1920×1080/30 FPS; SVG viewBox 1280×720. Scale tọa độ nhất quán, không trộn hai hệ tọa độ.
- Viền `#302b28`, nền kem `#faf0da`, da `#fff9e9`, tóc `#6c594d`, áo xanh `#81b5ca`, chăn `#91a28d`, highlight vàng `#f6d76c`. Xem profile cho bảng đầy đủ.
- Stroke đa số 2–4 đơn vị SVG, round cap/join. Nét phụ 1,2–2,5; tránh viền đều quá dày hay chi tiết dày đặc. Khối lớn màu phẳng, bóng chỉ giúp đọc chiều sâu.
- Font Patrick Hand, file TTF/OFL trong public/fonts. Label fixture 29 đơn vị SVG (~43,5 px output), ký hiệu to hơn. Không thay bằng chữ hệ thống hoặc chữ in sẵn trong ảnh.
- Nhân vật ngủ: Head trong final-minute.tsx; người giải thích đeo kính: Person trong rig-demo.tsx. Đây là hai model/vài trò riêng; đừng gán tóc/mặt khác nhau cho cùng một vai qua các shot.
- Room có tường hai mặt, đường sàn, giường/gối/chăn, cửa sổ/rèm, kệ/tranh, đồng hồ, tủ/đèn/cốc và cây tiền cảnh. Ánh sáng đổi cùng bầu trời/đồng hồ; không để đồng hồ 23:53 khi đã sáng.

## Chọn kiểu cảnh

| Ý trong voice | Cách dựng mặc định | Tránh |
| --- | --- | --- |
| Địa điểm, thời điểm | Toàn cảnh hoặc cận vật thể xác lập không gian | Title card không liên quan |
| Hành động cụ thể | Nhân vật thực hiện, đạo cụ tương tác | Người dẫn đọc + icon |
| Nhớ lại, phân tâm | Cutaway, hồi ức, tư tưởng hiện rồi mất | Giữ một hình gộp rất lâu |
| Giải thích cơ chế | Vật thể, sơ đồ đơn giản, so sánh | Tất cả thành bảng chữ |
| Hình ảnh hài hước | Ẩn dụ sân khấu/cuộc họp có diễn xuất | Thêm meme/SFX không phục vụ ý |
| Câu hỏi, phản biện | Người dẫn hoặc hai nhân vật phản ứng | Người dẫn tồn tại mọi shot |
| Chuyển thời gian | Bối cảnh biến đổi, ánh sáng, môi trường | Chỉ đổi caption |

Không bắt ép tỷ lệ % người dẫn, số cảnh/phút hay giới hạn độ dài mỗi cảnh. Bản chuẩn có 18 shot và người dẫn nói khoảng 6,7 giây cuối rải ở hai đoạn; đó là kết quả theo script, không phải quota.

## Chuyển động cụ thể

- Person: chu kỳ người dẫn 3,1 s, người nghe 3,7 s; nghiêng 1,35°/1,9°, bob ~1,4 đơn vị; lệch pha 1,7 rad. Đầu thêm ~1,1°, tay ~2–3° và có cử chỉ theo ý. Đây là giá trị khởi đầu khi nhân vật đứng nói, không áp lên mọi tư thế.
- Blink: fixture có các mốc 1,2/4,55/7,4/10,6 s và người nghe lệch 0,48 s. Với clip mới/dài hơn cần xây lịch mới hoặc lặp có chủ đích; đừng để hết blink sau 10 s.
- Miệng: voice RMS theo từng frame, ngưỡng ~0,019/0,065 cho Person; Head dùng ~0,025/0,065. Tính từ **voice sạch**, không từ mix SFX; đổi voice phải tính lại. Đóng miệng trong khoảng lặng.
- Bed: thở `sin(t*1.75)*2.1` đơn vị, rất nhẹ; đầu không lắc cùng nhịp người nói. Kéo chăn: mở/nắm tay → nâng điểm nắm và cạnh chăn → khuỷu tay gập → chăn/nếp vải theo tay → xoay đầu → siết mắt. Không để bàn tay rời mép chăn, xuyên vải hay sinh thêm tay.
- Seated: mỗi người pha riêng, nghiêng ~1,8°; phản ứng có ý khác nhau. Không cho tất cả cùng nói/cùng chớp.
- Camera: push-in nhẹ theo ý (fixture phòng ngủ ~1→1,055 trong 5,194 s); góc cận kéo chăn khác toàn cảnh. Không zoom liên tục xuyên tất cả shot.
- Transition: phần lớn cut theo ý; iris reveal 0,4 s ở một số cảnh, fade đầu 0,2 s và cuối ~0,28 s. Không thêm transition trang trí giữa từng câu.

## Text và SFX

Label fixture: reveal 0,28 s, dịch y 8→0, vệt highlight vẽ qua strokeDashoffset rồi chữ hiện theo ký tự. Dùng ngắn đủ đọc; chọn vị trí tránh mặt/tay/đạo cụ, chừa biên. Phân biệt thời điểm reveal, thời gian đọc và exit/shot cut. Các màu xanh nhạt/đỏ chỉ nhấn một ý.

SFX đi cùng sự kiện: tick đồng hồ, nắm/kéo vải, gối, click khóa, gõ phím, gạch bỏ, đổi cảnh, chim buổi sáng. Fixture có 32 placement / 31 file, hệ số SFX ~0,10–0,27 và voice 0,88; **không** lấy các hệ số đó thay cho kiểm tra loudness khi thay audio. SFX không lấn lời, không cắt đuôi thô, không gắn mỗi biến đổi animation một tiếng. Không lặp một pop cho mọi ý.
