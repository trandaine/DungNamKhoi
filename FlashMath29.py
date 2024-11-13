import tkinter as tk
import random
from tkinter import messagebox
import time
import threading

class MathTrainingApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720")
        self.root.title("FlashMath")
        
        self.font_size = tk.IntVar(value=120)
        self.level = None
        self.current_question = ""
        self.correct_answer = 0
        self.result_label = None
        
        self.setup_main_screen()
    
    def setup_main_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="Math Training App", font=("Arial", 36)).pack(pady=20)
        
        options_frame = tk.Frame(self.root)
        options_frame.pack(pady=20)
        
        tk.Label(options_frame, text="Font Size for Numbers:", font=("Arial", 28)).grid(row=0, column=0, padx=5)
        tk.Spinbox(options_frame, from_=10, to=200, textvariable=self.font_size, font=("Arial", 24), width=5).grid(row=0, column=1, padx=5)
        
        button_width = 20  # Chiều rộng của nút dài nhất
    
        tk.Button(self.root, text="ab + x", command=lambda: self.start_level("ab + x"), font=("Arial", 28), width=button_width).pack(pady=10)
        tk.Button(self.root, text="abc + xy", command=lambda: self.start_level("abc + xy"), font=("Arial", 28), width=button_width).pack(pady=10)
        tk.Button(self.root, text="abcd + xyz", command=lambda: self.start_level("abcd + xyz"), font=("Arial", 28), width=button_width).pack(pady=10)
        tk.Button(self.root, text="abcd + x00", command=lambda: self.start_level("abcd + x00"), font=("Arial", 28), width=button_width).pack(pady=10)

        
        bottom_frame = tk.Frame(self.root)
        bottom_frame.pack(side='bottom', anchor='sw', fill='x', padx=10, pady=10)
        
        tk.Button(bottom_frame, text="User Guide", command=self.show_user_guide, font=("Arial", 16)).pack(side='left', padx=5)
        tk.Button(bottom_frame, text="Back to MainPage", command=self.go_back_to_mainpage, font=("Arial", 16)).pack(side='left', padx=5)
    
    def start_level(self, level):
        self.level = level
        self.generate_question()
        self.show_question_screen()
    
    def generate_question(self):
        if self.level == "ab + x":
            while True:
                a = random.randint(10, 99)
                if a % 10 != 0:
                    break
            b = random.randint(1, 9)
            self.correct_answer = a + b
            self.current_question = f"{a} + {b}"
        
        elif self.level == "abc + xy":
            while True:
                a = random.randint(100, 999)
                if a % 100 != 0:
                    break
            b = random.randint(10, 99)
            self.correct_answer = a + b
            self.current_question = f"{a} + {b}"
        
        elif self.level == "abcd + xyz":
            a = random.randint(1000, 9999)
            b = random.randint(100, 999)
            self.correct_answer = a + b
            self.current_question = f"{a} + {b}"

        elif self.level == "abcd + x00":
            a = random.randint(1000, 9999)
            b = random.choice([100, 200, 300, 400, 500, 600, 700, 800, 900])
            self.correct_answer = a + b
            self.current_question = f"{a} + {b}"
    
    def show_question_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        question_label = tk.Label(self.root, text=self.current_question, font=("Arial", self.font_size.get()))
        question_label.pack(pady=20)
        
        self.user_answer = tk.Entry(self.root, font=("Arial", 28))
        self.user_answer.pack(pady=10)
        
        self.result_label = tk.Label(self.root, text="", font=("Arial", 24))
        self.result_label.pack(pady=10)
        
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=20)
        
        bottom_frame = tk.Frame(self.root)
        bottom_frame.pack(side='bottom', anchor='sw', fill='x', padx=10, pady=10)
        
        tk.Button(bottom_frame, text="Back", command=self.setup_main_screen, font=("Arial", 20)).pack(side='left', padx=5)
        tk.Button(control_frame, text="Check", command=self.check_answer, font=("Arial", 20)).grid(row=0, column=0, padx=5)
        tk.Button(control_frame, text="Next", command=lambda: [self.generate_question(), self.show_question_screen()], font=("Arial", 20)).grid(row=0, column=1, padx=5)
    
    def check_answer(self):
        try:
            user_sum = int(self.user_answer.get())
        except ValueError:
            user_sum = None
        
        if user_sum == self.correct_answer:
            self.result_label.config(text="Correct!", fg="green")
        else:
            self.result_label.config(text=f"Incorrect! Correct answer is {self.correct_answer}", fg="red")
    
    def show_user_guide(self):
        guide_text = """
User Guide:
1. Choose a training level from the main screen:
   - 'ab + x': Add a 2-digit number to a 1-digit number, not rounded (e.g., 31 + 4).
   - 'abc + xy': Add a 3-digit number to a 2-digit number, not rounded (e.g., 204 + 15).
   - 'abcd + xyz': Add a 4-digit number to a 3-digit number.
   - 'abcd + x00': Add a 4-digit number to a round hundred (e.g., 1324 + 200).

2. Once a level is chosen, a math question will be displayed immediately.
3. Enter your answer in the input box and press 'Check' to verify.
4. Press 'Next' to move on to a new question, or 'Back' to return to the main menu.
5. Adjust the font size for the numbers as needed from the main screen.

Good luck with your training!
"""
        guide_window = tk.Toplevel(self.root)
        guide_window.title("User Guide")
        guide_text_widget = tk.Text(guide_window, wrap="word", font=("Arial", 14))
        guide_text_widget.insert("1.0", guide_text)
        guide_text_widget.config(state="disabled")
        guide_text_widget.pack(expand=True, fill="both", padx=10, pady=10)
    
    def go_back_to_mainpage(self):
        app.setup_main_screen()

class FlashNumberTraining:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720")
        self.root.title("Flash Number Training")
        
        self.language = tk.StringVar(value="English")
        self.bg_color = tk.StringVar(value="white")
        self.digits_per_number = tk.IntVar(value=1)
        self.display_speed = tk.DoubleVar(value=1.0)
        self.num_to_display = tk.IntVar(value=10)
        self.allow_negative = tk.BooleanVar()
        self.font_size = tk.IntVar(value=120)
        self.calc_font_size = tk.IntVar(value=24)
        self.generated_numbers = []
        self.delayTime = 11         # Set the delay time
        self.startTime = None       # Set the start time when user start the session
        self.endTime = None         # Collect the end time when user end the session
        
        self.texts = {
            "English": {
                "digits_per_number": "Digits per Number:",
                "speed": "Speed (seconds):",
                "numbers_to_display": "Numbers to Display:",
                "font_size_for_numbers": "Font Size for Numbers:",
                "font_size_for_calculation": "Font Size for Calculation:",
                "allow_negative": "Allow Negative Numbers",
                "start_button": "Start",
                "your_answer": "Your Answer:",
                "submit_button": "Submit",
                "correct_answer": "Correct Answer:",
                "try_again_button": "Try Again",
                "stop_button": "Stop",
                "no_answer": "None",
                "user_guide": "User Guide",
                "guide_text": """
1. Language Selection: You can select the language for the app interface from the dropdown menu at the bottom of the screen.

2. Configure Settings: 
   - Digits per Number: Set the number of digits for each number shown in the flash training. (1 to 10 digits)
   - Speed: Set the speed in seconds at which the numbers are displayed. (0.1 to 10 seconds)
   - Numbers to Display: Set how many numbers you want to flash in the session.
   - Font Size for Numbers: Adjust the font size of the numbers displayed.
   - Font Size for Calculation: Adjust the font size of the calculation results.
   - Allow Negative Numbers: Choose whether or not to allow negative numbers in the session.

3. Start Countdown: Click on the Start button to begin the countdown. A 3-second countdown will start, displaying numbers 3, 2, and 1 before starting the flash training.

4. Flash Number Training: After the countdown, numbers will be displayed one by one at the speed you set. Try to remember them. You can stop the training anytime by clicking on the Stop button.

5. Answer Input: After the numbers are shown, enter the sum of all the numbers you saw into the input box and click Submit.

6. Results: The app will show the sum you entered, and compare it with the correct sum. If you made an error, you can try again by clicking on Try Again.

7. Stop Function: You can stop the flash number display anytime by clicking on the Stop button.

Tips: Practice regularly to improve your ability to recall numbers faster.

Troubleshooting: If the numbers are not displaying correctly or if the app freezes, try restarting the app.

Contact Support: If you need assistance or have questions, please contact our support team at Gmail: thienlydoncoi@gmail.com.
                """
            },
            "Tiếng Việt": {
                "digits_per_number": "Số chữ số mỗi số:",
                "speed": "Tốc độ (giây):",
                "numbers_to_display": "Số lượng hiển thị:",
                "font_size_for_numbers": "Kích thước chữ số:",
                "font_size_for_calculation": "Kích thước chữ tính toán:",
                "allow_negative": "Cho phép số âm",
                "start_button": "Bắt đầu",
                "your_answer": "Đáp án của bạn:",
                "submit_button": "Gửi",
                "correct_answer": "Đáp án đúng:",
                "try_again_button": "Thử lại",
                "stop_button": "Dừng",
                "no_answer": "Không có",
                "user_guide": "Hướng Dẫn",
                "guide_text": """
1. Chọn Ngôn Ngữ: Bạn có thể chọn ngôn ngữ giao diện ứng dụng từ menu thả xuống ở dưới cùng của màn hình.

2. Cấu Hình Cài Đặt: 
   - Số Chữ Số Mỗi Số: Cài đặt số lượng chữ số mỗi số hiển thị trong bài tập flash training. (1 đến 10 chữ số)
   - Tốc Độ: Cài đặt tốc độ (giây) hiển thị các số. (0.1 đến 10 giây)
   - Số Lượng Hiển Thị: Cài đặt số lượng số bạn muốn hiển thị trong buổi tập.
   - Kích Thước Chữ Số: Điều chỉnh kích thước chữ cho các số hiển thị.
   - Kích Thước Chữ Tính Toán: Điều chỉnh kích thước chữ cho kết quả tính toán.
   - Cho Phép Số Âm: Chọn có cho phép số âm trong buổi tập hay không.

3. Đếm Ngược: Nhấn nút Bắt Đầu để bắt đầu đếm ngược. Một đếm ngược 3 giây sẽ bắt đầu, hiển thị các số 3, 2 và 1 trước khi bắt đầu bài tập flash training.

4. Bài Tập Flash Number: Sau khi đếm ngược xong, các số sẽ được hiển thị lần lượt theo tốc độ bạn cài đặt. Cố gắng ghi nhớ chúng. Bạn có thể dừng bài tập bất cứ lúc nào bằng cách nhấn nút Dừng.

5. Nhập Đáp Án: Sau khi các số được hiển thị, nhập tổng số các số bạn đã thấy vào ô nhập và nhấn Gửi.

6. Kết Quả: Ứng dụng sẽ hiển thị tổng số bạn đã nhập và so sánh với tổng số đúng. Nếu bạn sai, bạn có thể thử lại bằng cách nhấn nút Thử lại.

7. Chức Năng Dừng: Bạn có thể dừng hiển thị số bất cứ lúc nào bằng cách nhấn nút Dừng.

Mẹo: Luyện tập thường xuyên để cải thiện khả năng ghi nhớ số nhanh hơn.

Khắc Phục Sự Cố: Nếu các số không hiển thị đúng hoặc ứng dụng bị treo, hãy thử khởi động lại ứng dụng.

Liên Hệ Hỗ Trợ: Nếu bạn cần hỗ trợ hoặc có câu hỏi, vui lòng liên hệ với đội ngũ hỗ trợ của chúng tôi qua Gmail: thienlydoncoi@gmail.com.
                """
            }
        }
        
        self.stop_display = False
        
        self.setup_selection_screen()
    
    def setup_selection_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        options_frame = tk.Frame(self.root)
        options_frame.pack(pady=20)
        
        language = self.language.get()
        texts = self.texts[language]
        
        tk.Label(options_frame, text=texts["digits_per_number"], font=("Arial", 28)).grid(row=0, column=0, sticky="e", padx=5)
        tk.Spinbox(options_frame, from_=1, to=10, textvariable=self.digits_per_number, font=("Arial", 24), width=5).grid(row=0, column=1, padx=5)
        
        tk.Label(options_frame, text=texts["speed"], font=("Arial", 28)).grid(row=1, column=0, sticky="e", padx=5)
        tk.Spinbox(options_frame, from_=0.1, to=10.0, increment=0.1, textvariable=self.display_speed, font=("Arial", 24), width=5).grid(row=1, column=1, padx=5)
        
        tk.Label(options_frame, text=texts["numbers_to_display"], font=("Arial", 28)).grid(row=2, column=0, sticky="e", padx=5)
        tk.Spinbox(options_frame, from_=1, to=100, textvariable=self.num_to_display, font=("Arial", 24), width=5).grid(row=2, column=1, padx=5)
        
        tk.Label(options_frame, text=texts["font_size_for_numbers"], font=("Arial", 28)).grid(row=3, column=0, sticky="e", padx=5)
        tk.Spinbox(options_frame, from_=10, to=200, textvariable=self.font_size, font=("Arial", 24), width=5).grid(row=3, column=1, padx=5)
        
        tk.Label(options_frame, text=texts["font_size_for_calculation"], font=("Arial", 28)).grid(row=4, column=0, sticky="e", padx=5)
        tk.Spinbox(options_frame, from_=10, to=100, textvariable=self.calc_font_size, font=("Arial", 24), width=5).grid(row=4, column=1, padx=5)
        
        tk.Checkbutton(options_frame, text=texts["allow_negative"], variable=self.allow_negative, font=("Arial", 24)).grid(row=5, columnspan=2, pady=10)
        
        tk.Button(self.root, text=texts["start_button"], command=self.start_countdown, font=("Arial", 28)).pack(pady=20)
        
        bottom_frame = tk.Frame(self.root)
        bottom_frame.pack(side="bottom", fill="x", padx=10, pady=10)
        
        guide_button = tk.Button(bottom_frame, text=texts["user_guide"], command=self.show_user_guide, font=("Arial", 16))
        guide_button.pack(side="left", padx=10)
        
        language_menu = tk.OptionMenu(bottom_frame, self.language, "English", "Tiếng Việt", command=self.update_language)
        language_menu.pack(side="right", padx=10)
        
        tk.Button(bottom_frame, text="Back to MainPage", command=self.go_back_to_mainpage, font=("Arial", 16)).pack(side='left', padx=5)
    
    def update_language(self, value):
        self.setup_selection_screen()
    
    def show_user_guide(self):
        language = self.language.get()
        guide_text = self.texts[language]["guide_text"]
        
        guide_window = tk.Toplevel(self.root)
        guide_window.title(self.texts[language]["user_guide"])
        guide_text_widget = tk.Text(guide_window, wrap="word", font=("Arial", 14))
        guide_text_widget.insert("1.0", guide_text)
        guide_text_widget.config(state="disabled")
        guide_text_widget.pack(expand=True, fill="both", padx=10, pady=10)

    
    def start_countdown(self):
        self.stop_display = False
        self.countdown_number = 3
        self.show_countdown()
    
    def show_countdown(self):
        if self.stop_display:
            self.setup_selection_screen()
            return
        
        for widget in self.root.winfo_children():
            widget.destroy()
        
        colors = {3: "red", 2: "yellow", 1: "blue"}
        font_size = self.font_size.get()
        
        countdown_label = tk.Label(self.root, text=str(self.countdown_number), font=("Arial", font_size), fg=colors[self.countdown_number])
        countdown_label.pack(expand=True)
        
        stop_button_frame = tk.Frame(self.root)
        stop_button_frame.pack(side="bottom", pady=20)
        
        stop_button = tk.Button(stop_button_frame, text=self.texts[self.language.get()]["stop_button"], command=self.stop, font=("Arial", 24))
        stop_button.pack()
        
        if self.countdown_number > 1:
            self.countdown_number -= 1
            self.root.after(700, self.show_countdown)
        else:
            self.root.after(700, lambda: countdown_label.pack_forget())
            self.root.after(1700, self.start_display)
    
    def start_display(self):
        self.stop_display = False
        self.generated_numbers.clear()
        
        num_digits = self.digits_per_number.get()
        num_count = self.num_to_display.get()
        allow_neg = self.allow_negative.get()
        
        previous_number = None
        for _ in range(num_count):
            while True:
                number = random.randint(10**(num_digits-1), 10**num_digits - 1)
                if allow_neg and random.choice([True, False]):
                    number = -number
                if number != previous_number:
                    break
            self.generated_numbers.append(number)
            previous_number = number
        
        self.current_index = 0
        self.show_next_number()
    
    def show_next_number(self):
        if self.stop_display:
            self.setup_selection_screen()
            return
        if self.current_index >= len(self.generated_numbers):
            self.show_result_screen()
            return
        
        for widget in self.root.winfo_children():
            widget.destroy()
        
        number = self.generated_numbers[self.current_index]
        font_size = self.font_size.get()
        number_label = tk.Label(self.root, text=str(number), font=("Arial", font_size))
        number_label.pack(expand=True)
        
        stop_button_frame = tk.Frame(self.root)
        stop_button_frame.pack(side="bottom", pady=20)
        
        stop_button = tk.Button(stop_button_frame, text=self.texts[self.language.get()]["stop_button"], command=self.stop, font=("Arial", 24))
        stop_button.pack()
        
        self.current_index += 1
        self.root.after(int(self.display_speed.get() * 1000), self.show_next_number)


    # Function start counting the time when show_next_number complete
    def startCountdownUserTime(self):
        self.startTime = time.time()

    def submit_button_clicked(self):
        self.endTime = time.time()
        if self.startTime is not None and self.endTime is not None:
            elapsed_time = self.endTime - self.startTime
            print(f"You spent {elapsed_time:.2f} seconds to complete")
            messagebox.showinfo("Elapsed Time", f"You spent {elapsed_time:.2f} seconds to complete")
        else:
            print("Timer was not started properly.")


    def stop(self):
        self.stop_display = True
    
    def show_result_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # correct_sum = sum(self.generated_numbers)
        
        language = self.language.get()
        texts = self.texts[language]
        
        tk.Label(self.root, text=texts["your_answer"], font=("Arial", 28)).pack(pady=10)
        self.user_answer = tk.Entry(self.root, font=("Arial", 28))
        self.user_answer.pack(pady=10)
        tk.Button(self.root, text=texts["submit_button"], command=lambda: [self.startCountDelayTime(), self.submit_button_clicked()], font=("Arial", 28)).pack(pady=10)
        
        stop_button_frame = tk.Frame(self.root)
        stop_button_frame.pack(side="bottom", pady=20)
        
        tk.Button(stop_button_frame, text=texts["stop_button"], command=self.stop, font=("Arial", 24)).pack()
        self.startCountdownUserTime()

    
    def startCountDelayTime(self):
        correct_sum = sum(self.generated_numbers)

        def countdown():
            for remaining in range(self.delayTime, 0, -1):
                print(f"Time remaining: {remaining} seconds")
                time.sleep(1)
            self.check_answer(correct_sum)

        countdown_thread = threading.Thread(target=countdown)
        countdown_thread.start()

    

    def check_answer(self, correct_sum):
        try:
            user_sum = int(self.user_answer.get())
        except ValueError:
            user_sum = None
        
        if user_sum is None:
            user_sum_display = self.texts[self.language.get()]["no_answer"]
        else:
            user_sum_display = str(user_sum)
        
        for widget in self.root.winfo_children():
            widget.destroy()
        
        language = self.language.get()
        texts = self.texts[language]
        
        tk.Label(self.root, text=f"{texts['your_answer']} {user_sum_display}", font=("Arial", 28)).pack(pady=10)
        tk.Label(self.root, text=f"{texts['correct_answer']} {correct_sum}", font=("Arial", 28)).pack(pady=10)
        
        num_display_frame = tk.Frame(self.root)
        num_display_frame.pack(pady=10, fill="both", expand=True)
        
        num_display = " + ".join(f"({n})" if n < 0 else str(n) for n in self.generated_numbers)
        calc_font_size = self.calc_font_size.get()
        num_display_text = tk.Text(num_display_frame, font=("Arial", calc_font_size), wrap="word", height=10, width=100)
        num_display_text.insert("1.0", num_display)
        num_display_text.config(state="disabled")
        num_display_text.pack(fill="both", expand=True)
        
        tk.Button(self.root, text=texts["try_again_button"], command=self.setup_selection_screen, font=("Arial", 28)).pack(pady=20)

    def go_back_to_mainpage(self):
        app.setup_main_screen()

class FlashMathApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720")
        self.root.title("FlashMath")
        self.setup_main_screen()
    
    def setup_main_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="FlashMath", font=("Arial", 36)).pack(pady=20)
        
        tk.Button(self.root, text="Math Training", command=self.start_math_training, font=("Arial", 28)).pack(pady=10)
        tk.Button(self.root, text="Flash Number", command=self.start_flash_number, font=("Arial", 28)).pack(pady=10)
    
    def start_math_training(self):
        self.math_app = MathTrainingApp(self.root)
    
    def start_flash_number(self):
        self.flash_number_app = FlashNumberTraining(self.root)

# Khởi chạy ứng dụng chính
root = tk.Tk()
app = FlashMathApp(root)
root.mainloop()
