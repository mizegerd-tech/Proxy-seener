

## README - English Version

### Overview

This project is a Python-based script that automates the process of increasing view counts on Telegram posts using proxies. The script fetches the required data from a Telegram post and then sends a request to increase the view count. It uses threading to handle multiple proxies concurrently, making it faster and more efficient.

### Features

- **Proxy Support**: The script reads proxies from a file (`proxy.txt`) and uses them to send view requests.
- **Threading**: Uses threading to handle multiple proxies at the same time, improving speed and efficiency.
- **Customizable Thread Limit**: You can adjust the number of threads by changing the `Semaphore` value.

### Requirements

- Python 3.x
- `requests` library: You can install it using `pip install requests`.

### Setup and Usage

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install required dependencies**:
   Make sure you have the `requests` library installed:
   ```bash
   pip install requests
   ```

3. **Prepare the `proxy.txt` file**:
   Create a file called `proxy.txt` in the root directory of the project. Add your proxies to this file, one per line in the following format:
   ```
   123.123.123.123:8080
   234.234.234.234:8000
   ```

4. **Run the script**:
   Use the following command to run the script:
   ```bash
   python script.py <channel_name> <post_number>
   ```
   - `<channel_name>`: The Telegram channel name (without the '@' symbol).
   - `<post_number>`: The post number in the channel.

   Example:
   ```bash
   python script.py example_channel 123
   ```

### Configuration

- **Thread Limit**: By default, the thread limit is set to 500 in the following line:
  ```python
  max = threading.Semaphore(value=500)
  ```
  You can reduce this value if you encounter CPU/RAM issues on your system.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## README - نسخه فارسی

### معرفی

این پروژه یک اسکریپت پایتون است که برای افزایش تعداد بازدیدهای پست‌های تلگرام با استفاده از پروکسی‌ها طراحی شده است. این اسکریپت اطلاعات مورد نیاز را از یک پست تلگرامی دریافت کرده و سپس درخواست افزایش تعداد بازدید را ارسال می‌کند. این پروژه با استفاده از **چند ریسمانی (Threading)** کار می‌کند تا از چندین پروکسی به صورت همزمان استفاده کند و عملکرد سریع‌تری داشته باشد.

### ویژگی‌ها

- **پشتیبانی از پروکسی**: اسکریپت پروکسی‌ها را از فایلی به نام `proxy.txt` خوانده و از آنها برای ارسال درخواست‌های بازدید استفاده می‌کند.
- **چند ریسمانی (Threading)**: از چندین ریسمان برای مدیریت همزمان پروکسی‌ها استفاده می‌کند که باعث بهبود سرعت و کارایی می‌شود.
- **قابل تنظیم بودن تعداد ریسمان‌ها**: می‌توانید تعداد ریسمان‌ها را با تغییر مقدار `Semaphore` تنظیم کنید.

### پیش‌نیازها

- پایتون 3.x
- کتابخانه `requests`: می‌توانید آن را با دستور زیر نصب کنید:
   ```bash
   pip install requests
   ```

### راه‌اندازی و استفاده

1. **کلون کردن مخزن**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **نصب وابستگی‌ها**:
   اطمینان حاصل کنید که کتابخانه `requests` نصب شده باشد:
   ```bash
   pip install requests
   ```

3. **آماده‌سازی فایل `proxy.txt`**:
   فایلی با نام `proxy.txt` در دایرکتوری اصلی پروژه ایجاد کنید. پروکسی‌های خود را در این فایل وارد کنید، هر پروکسی در یک خط به فرمت زیر:
   ```
   123.123.123.123:8080
   234.234.234.234:8000
   ```

4. **اجرای اسکریپت**:
   از دستور زیر برای اجرای اسکریپت استفاده کنید:
   ```bash
   python script.py <channel_name> <post_number>
   ```
   - `<channel_name>`: نام کانال تلگرام (بدون علامت '@').
   - `<post_number>`: شماره پست در کانال.

   مثال:
   ```bash
   python script.py example_channel 123
   ```

### تنظیمات

- **تعداد ریسمان‌ها**: به صورت پیش‌فرض، تعداد ریسمان‌ها برابر با 500 تنظیم شده است. می‌توانید این مقدار را در خط زیر تغییر دهید:
  ```python
  max = threading.Semaphore(value=500)
  ```
  اگر با مشکلات مربوط به CPU یا RAM مواجه شدید، این مقدار را کاهش دهید.

### لایسنس

این پروژه تحت مجوز MIT منتشر شده است. برای جزئیات بیشتر فایل [LICENSE](LICENSE) را ببینید.

