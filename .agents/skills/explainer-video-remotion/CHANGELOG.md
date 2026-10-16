# Thay đổi v2.0.0

- Chốt profile sleep-final-1m-v1 từ bản final 62,4 giây thay cho các demo v1/v2/v3.
- Tách chế độ tái tạo nguyên bản và dựng nội dung mới cùng phong cách.
- Lưu source/tài nguyên chạy được, hash bản chuẩn, phiên bản dependencies và cấu hình render.
- Thêm quy tắc chọn kiểu cảnh theo ý: hạn chế bố cục người dẫn + bảng, diễn xuất trực tiếp, đa dạng góc/bối cảnh/vật thể/ẩn dụ.
- Định lượng màu, font, nét, motion/biểu cảm, nhịp text/SFX; chỉ rõ giá trị nào là fixture, không áp quota cho script mới.
- Thêm bootstrap không ghi đè, kiểm tra bundle và validator timing/media cho composition mới.
- Gỡ mặc định hỏi duyệt sau 30 giây khi user đã giao phạm vi rõ ràng; giữ voice/SRT gốc và tính lại timing cho nội dung mới.
- Nêu đúng giới hạn RMS lip-sync, tệp mẫu chưa truy cập và khả năng MP4 khác byte giữa các môi trường.

## Kiểm chứng trong phiên cập nhật

Đã kiểm archive/source SHA-256, liên kết nội bộ và dữ liệu 18 shot/32 SFX; giải nén độc lập và validate manifest; TypeScript đạt. Dùng dependencies sẵn có đúng version để render lại frame 1410 từ dự án giải nén: khớp pixel với khung hình tham chiếu đã lưu. Đã kiểm bootstrap từ chối ghi đè thư mục có dữ liệu. Không cài mới dependencies hoặc render lại toàn bộ clip ở bước cập nhật skill; MP4 chuẩn là file đã xuất và kiểm trước đó.
