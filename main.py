def is_leap_year(year):
    """Kiểm tra xem năm có phải là năm nhuận hay không."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    """Trả về số ngày trong tháng, bao gồm việc xử lý tháng 2 đặc biệt."""
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in {4, 6, 9, 11}:  
        return 30
    else:  
        return 31

def validate_date(year, month, day):
    """Kiểm tra tính hợp lệ của ngày tháng năm."""
    if not (1850 <= year <= 2050):
        return "Error: Year out of range"
    if not (1 <= month <= 12):
        return "Error: Month out of range"
    if not (1 <= day <= days_in_month(month, year)):
        return f"Error: Invalid date {year}-{month}-{day}"
    return None

def next_date(year, month, day):
    """Trả về ngày kế tiếp của một ngày cho trước."""
    error = validate_date(year, month, day)
    if error:
        return error

    if day < days_in_month(month, year):
        return f"{year}-{month:02d}-{day + 1:02d}"
    elif month < 12:
        return f"{year}-{month + 1:02d}-01"
    else:  
        return f"{year + 1}-01-01"

# Phần kiểm thử
def run_tests(test_cases, test_name):
    print(f"\nRunning {test_name}:")
    for year, month, day, expected in test_cases:
        result = next_date(year, month, day)
        status = "PASS" if result == expected else "FAIL"
        print(f"Input: {year}-{month:02d}-{day:02d}, Expected: {expected}, Got: {result}, Status: {status}")

#  Phân vùng tương đương
eq_classes = [
    (2023, 4, 15, "2023-04-16"),  # Tháng 30 ngày
    (2023, 4, 30, "2023-05-01"),  # Ngày cuối tháng 30 ngày
    (2023, 1, 31, "2023-02-01"),  # Ngày cuối tháng 31 ngày
    (2023, 2, 15, "2023-02-16"),  # Tháng 2, năm không nhuận
    (2023, 2, 28, "2023-03-01"),  # Cuối tháng 2, năm không nhuận
    (2024, 2, 28, "2024-02-29"),  # Tháng 2, năm nhuận
    (2024, 2, 29, "2024-03-01"),  # Cuối tháng 2, năm nhuận
    (2023, 12, 31, "2024-01-01"),  # Chuyển sang năm mới
]

#  Phân tích giá trị biên
boundary_cases = [
    (1850, 1, 1, "1850-01-02"),   # Năm nhỏ nhất hợp lệ
    (2050, 12, 31, "2051-01-01"),  # Năm lớn nhất hợp lệ
    (1849, 12, 31, "Error: Year out of range"),  # Năm dưới giới hạn
    (2051, 1, 1, "Error: Year out of range"),    # Năm trên giới hạn
    (2023, 0, 1, "Error: Month out of range"),   # Tháng dưới giới hạn
    (2023, 13, 1, "Error: Month out of range"),  # Tháng trên giới hạn
    (2023, 1, 0, "Error: Invalid date 2023-1-0"),     # Ngày dưới giới hạn
    (2023, 1, 32, "Error: Invalid date 2023-1-32"),  # Ngày trên giới hạn
]

#  Bảng quyết định
decision_table = [
    (2023, 5, 15, "2023-05-16"),  # Ngày bình thường
    (2023, 4, 30, "2023-05-01"),  # Cuối tháng 30 ngày
    (2023, 3, 31, "2023-04-01"),  # Cuối tháng 31 ngày
    (2023, 12, 31, "2024-01-01"),  # Cuối năm
    (2023, 2, 28, "2023-03-01"),  # Cuối tháng 2, năm không nhuận
    (2024, 2, 29, "2024-03-01"),  # Cuối tháng 2, năm nhuận
    (2023, 2, 30, "Error: Invalid date 2023-2-30"),  # Ngày không hợp lệ
]

# Chạy kiểm thử
run_tests(eq_classes, "Equivalence Class Tests")
run_tests(boundary_cases, "Boundary Value Tests")
run_tests(decision_table, "Decision Table Tests")
