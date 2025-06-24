



from flask import Flask, render_template, request 
import json
import os

app = Flask(__name__)

@app.route('/')
def الصفحة_الرئيسية():
    return render_template('home.html')

@app.route('/about')
def عن_العيادة():
    return render_template('about.html')

@app.route('/form', methods=['GET', 'POST'])
def form_page():
    if request.method == 'POST':
        # 1. التقاط البيانات من النموذج
        name = request.form['name']
        pet = request.form['pet']
        reason = request.form['reason']
        date = request.form['date']
        time = request.form['time']

        # 2. بناء سجل الموعد كقاموس
        new_appointment = {
            "name": name,
            "pet": pet,
            "reason": reason,
            "date": date,
            "time": time
        }

        # 3. قراءة الملف الحالي أو إنشاء قائمة جديدة إذا ما كان موجود
        file_path = 'appointments.json'
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read().strip()
                appointments = json.loads(content)if content else[]
        else:
            appointments = []

        # 4. إضافة الموعد الجديد
        appointments.append(new_appointment)

        # 5. حفظ التحديث في نفس الملف
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(appointments, file, ensure_ascii=False, indent=2)

        return "✅ تم حفظ الموعد بنجاح!"

    return render_template('form.html')



@app.route('/appointments')
def عرض_المواعيد():
    file_path = 'appointments.json'
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            appointments = json.load(file)
    else:
        appointments = []
    
    return render_template('appointments.html', appointments=appointments)



if __name__ == '__main__':
    app.run(debug=True)

