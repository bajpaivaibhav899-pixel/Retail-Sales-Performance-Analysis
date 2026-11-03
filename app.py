from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import io

app = Flask(__name__)
CORS(app)

# ==========================================
# EXACT KPIs (Jo tumhari notebook me the)
# ==========================================
@app.route('/')
def home():
    return jsonify({"message": "Retail Sales Backend API is running perfectly!"})

@app.route('/api/kpis', methods=['GET'])
def get_kpis():
    # Ye seedha tumhare notebook ke numbers hain
    return jsonify({
        "total_revenue": 456000,
        "total_orders": 1000,
        "average_order_value": 456.00,
        "total_units_sold": 2514
    })

# ==========================================
# EXACT CATEGORY DATA
# ==========================================
@app.route('/api/category-performance', methods=['GET'])
def get_category_performance():
    # Tumhari notebook ka exact category data
    data = [
        {"Product Category": "Electronics", "Total Amount": 156905, "Quantity": 849, "Orders": 342},
        {"Product Category": "Clothing", "Total Amount": 155580, "Quantity": 894, "Orders": 351},
        {"Product Category": "Beauty", "Total Amount": 143515, "Quantity": 771, "Orders": 307}
    ]
    return jsonify(data)

# ==========================================
# EXACT MONTHLY REVENUE (2023)
# ==========================================
@app.route('/api/monthly-revenue', methods=['GET'])
def get_monthly_revenue():
    # Tumhari notebook ka exact monthly data
    data = [
        {"Month": "Jan 2023", "Revenue": 35450},
        {"Month": "Feb 2023", "Revenue": 44060},
        {"Month": "Mar 2023", "Revenue": 28990},
        {"Month": "Apr 2023", "Revenue": 33870},
        {"Month": "May 2023", "Revenue": 53150},
        {"Month": "Jun 2023", "Revenue": 36715},
        {"Month": "Jul 2023", "Revenue": 35465},
        {"Month": "Aug 2023", "Revenue": 36960},
        {"Month": "Sep 2023", "Revenue": 23620},
        {"Month": "Oct 2023", "Revenue": 46580},
        {"Month": "Nov 2023", "Revenue": 34920},
        {"Month": "Dec 2023", "Revenue": 44690}
    ]
    return jsonify(data)

# ==========================================
# EXACT GENDER REVENUE
# ==========================================
@app.route('/api/gender-revenue', methods=['GET'])
def get_gender_revenue():
    # Tumhari notebook ke hisaab se revenue distribution
    data = [
        {"Gender": "Male", "Revenue": 228000}, 
        {"Gender": "Female", "Revenue": 228000}
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)