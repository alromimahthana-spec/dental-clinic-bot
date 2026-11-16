# بوت حجز عيادة أسنان - ثناء | thanaa.codes

print("=" * 40)
print("🦷 عيادة ثناء لطب الأسنان - اهلا فيك")
print("=" * 40)

print("\n✨ خدمات العيادة:")
print("1. كشف وتشخيص - 50 ريال")
print("2. تنظيف الأسنان - 150 ريال")
print("3. حشوة - 200 ريال")
print("4. خلع ضرس - 250 ريال")
print("5. تقويم أسنان - استشارة مجانية")
print("6. تبييض أسنان - 600 ريال")
print("7. تركيب - 800 ريال")

choice = input("\nاختار رقم الخدمة: ")

services = {
    "1": ("كشف وتشخيص", 50),
    "2": ("تنظيف الأسنان", 150),
    "3": ("حشوة", 200),
    "4": ("خلع ضرس", 250),
    "5": ("تقويم أسنان", 0),
    "6": ("تبييض أسنان", 600),
    "7": ("تركيب", 800),
}

service_name, service_price = services.get(choice, ("غير معروفة", 0))
print(f"\nاخترت: {service_name} - {service_price} ريال")

print("\n👨‍⚕️ اختار الدكتور:")
print("1. د. أحمد - عام")
print("2. د. سارة - تجميل")
print("3. د. محمد - تقويم")
print("4. د. نورة - أطفال")

doctor_choice = input("اختار الدكتور: ")
doctors = {"1":"د. أحمد - عام","2":"د. سارة - تجميل","3":"د. محمد - تقويم","4":"د. نورة - أطفال"}
doctor_name = doctors.get(doctor_choice, "د. أحمد - عام")

print("\n📅 اليوم:")
print("1. السبت")
print("2. الأحد")
print("3. الاثنين")
print("4. الثلاثاء")
print("5. الأربعاء")
print("6. الخميس")

day_choice = input("اختار اليوم: ")
days = {"1":"السبت","2":"الأحد","3":"الاثنين","4":"الثلاثاء","5":"الأربعاء","6":"الخميس"}
day_name = days.get(day_choice, "السبت")

print("\n🕐 الوقت:")
print("1. 9 صباحا")
print("2. 11 صباحا")
print("3. 1 ظهرا")
print("4. 4 عصرا")
print("5. 6 مساء")
print("6. 8 مساء")

time_choice = input("اختار الوقت: ")
times = {"1":"9 صباحا","2":"11 صباحا","3":"1 ظهرا","4":"4 عصرا","5":"6 مساء","6":"8 مساء"}
time_name = times.get(time_choice, "9 صباحا")

print("\n--- بيانات المريض ---")
name = input("اسمك: ")
phone = input("رقم جوالك: ")
age = input("عمرك: ")

print("\n" + "=" * 40)
print("✅ تم تأكيد حجزك!")
print("=" * 40)
print(f"الاسم: {name}")
print(f"الجوال: {phone}")
print(f"العمر: {age}")
print(f"الخدمة: {service_name}")
print(f"الدكتور: {doctor_name}")
print(f"اليوم: {day_name}")
print(f"الوقت: {time_name}")
print(f"السعر: {service_price} ريال")
print("\nنراك قريبا في العيادة 🦷💖")
print("ارجو الحضور قبل الموعد بـ 10 دقائق")
print("=" * 40)
