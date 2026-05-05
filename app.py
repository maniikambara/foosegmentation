import streamlit as st
import cv2
import numpy as np
from PIL import Image
import os
from pathlib import Path
import socket

try:
    from ultralytics import YOLO
    YOLO_AVAILABLE = True
except ImportError:
    YOLO_AVAILABLE = False

try:
    socket.setdefaulttimeout(30)
except:
    pass

FOOD_BENEFITS = {
    "rice": "Source of complex carbohydrates, providing sustained energy. Rich in minerals like magnesium and phosphorus.",
    "bread": "Source of fiber and vitamin B. Aids digestion and provides energy. Rich in carbohydrates.",
    "noodles": "Source of carbohydrates. Choose whole grain varieties for better health benefits.",
    "sushi": "Fish protein source, omega-3 for heart health. Rich in antioxidants from seaweed.",
    "curry": "Contains turmeric with strong anti-inflammatory properties. Boosts metabolism and immunity.",
    "pasta": "Complex carbohydrates, energy source. Choose whole wheat pasta for higher fiber.",
    "salad": "Low calorie, rich in fiber and vitamins. Good for diet and digestive health.",
    "chicken": "High protein, low fat. Rich in niacin and selenium for muscle health.",
    "beef": "High quality protein, rich in iron to prevent anemia. Source of vitamin B12.",
    "fish": "High quality protein, omega-3 for heart and brain health. Rich in vitamin D.",
    "vegetable": "Rich in fiber, vitamins, and minerals. Low calorie, good for digestive health.",
    "fruit": "Source of vitamins, minerals, and antioxidants. High in fiber for digestive health.",
    "dessert": "High in sugar and calories. Enjoy in limited quantities as occasional snacks.",
    "cake": "High in calories, sugar, and fat. Better enjoyed occasionally as dessert.",
    "pizza": "Carbohydrates from bread, protein from cheese. Ensure toppings are balanced between vegetables and protein.",
    "egg": "Complete protein, rich in choline for brain health. Lutein for eye health.",
    "milk": "Rich in calcium for strong bones. Source of protein and vitamin D.",
    "cheese": "Rich in calcium and protein. High in fat, consume in moderation.",
    "soup": "Complete nutrition in warm dish. Easy to digest and helps with hydration.",
    "ramen": "Carbohydrates from noodles, protein from broth. Choose balanced nutrition versions.",
    "donut": "High in fat and sugar, high calories. Enjoy occasionally only, not as daily food.",
    "burger": "Protein from meat, carbohydrates from bread. Adjust toppings for nutritional balance.",
    "sandwich": "Flexible with nutrition - depends on filling. Choose whole grain bread and nutritious fillings.",
    "spaghetti": "Carbohydrates, add protein and vegetables for complete nutrition.",
    "dumpling": "Combination of protein and carbohydrates. Control portions due to medium to high calories.",
    "tofu": "Complete plant protein, low fat. Rich in iron for vegetarians.",
    "tempeh": "Plant protein, easy to digest. Natural probiotics for gut health.",
}

st.set_page_config(
    page_title="Food Detection App",
    page_icon="plate_with_cutlery",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    .food-info {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        border-left: 5px solid #FF6B6B;
    }
    .detection-result {
        background-color: #e8f5e9;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
        border-left: 5px solid #4caf50;
    }
    .confidence-high {
        color: #4caf50;
        font-weight: bold;
    }
    .confidence-medium {
        color: #ffa726;
        font-weight: bold;
    }
    .confidence-low {
        color: #ef5350;
        font-weight: bold;
    }
    .demo-mode {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        border-left: 5px solid #ffc107;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    """Load trained YOLOv8 model"""
    if not YOLO_AVAILABLE:
        return None
        
    model_path = "models/uecfoodpix_v1/weights/best.pt"
    
    if not os.path.exists(model_path):
        return None
    
    try:
        model = YOLO(model_path)
        return model
    except Exception as e:
        return None

def detect_food_from_image(image):
    """Demo mode - detect food by color and shape analysis"""
    img_array = np.array(image)
    
    hsv = cv2.cvtColor(img_array, cv2.COLOR_RGB2HSV)
    
    lower_brown = np.array([10, 50, 50])
    upper_brown = np.array([25, 255, 255])
    brown_mask = cv2.inRange(hsv, lower_brown, upper_brown)
    
    lower_green = np.array([35, 50, 50])
    upper_green = np.array([85, 255, 255])
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])
    red_mask1 = cv2.inRange(hsv, lower_red, upper_red)
    
    lower_red2 = np.array([170, 50, 50])
    upper_red2 = np.array([180, 255, 255])
    red_mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    red_mask = cv2.bitwise_or(red_mask1, red_mask2)
    
    detections = []
    
    brown_pixels = cv2.countNonZero(brown_mask)
    green_pixels = cv2.countNonZero(green_mask)
    red_pixels = cv2.countNonZero(red_mask)
    
    total_pixels = brown_pixels + green_pixels + red_pixels
    
    if total_pixels > 0:
        brown_ratio = brown_pixels / total_pixels
        green_ratio = green_pixels / total_pixels
        red_ratio = red_pixels / total_pixels
        
        if brown_ratio > 0.3:
            detections.append(("chicken", min(0.7 + brown_ratio * 0.2, 0.95)))
        
        if green_ratio > 0.2:
            detections.append(("vegetable", min(0.6 + green_ratio * 0.3, 0.90)))
        
        if red_ratio > 0.2:
            detections.append(("food_item", min(0.65 + red_ratio * 0.25, 0.92)))
    
    if len(detections) == 0:
        detections.append(("food_item", 0.65))
    
    return sorted(detections, key=lambda x: x[1], reverse=True)

def get_food_benefit(food_name):
    """Get health benefits for detected food"""
    food_name_lower = food_name.lower().strip()
    
    if food_name_lower in FOOD_BENEFITS:
        return FOOD_BENEFITS[food_name_lower]
    
    for food, benefit in FOOD_BENEFITS.items():
        if food in food_name_lower or food_name_lower in food:
            return benefit
    
    return "Nutritious food with health benefits. Consume in balanced portions with other nutrients."

def get_confidence_color(confidence):
    """Get color based on confidence level"""
    if confidence >= 0.7:
        return "confidence-high"
    elif confidence >= 0.5:
        return "confidence-medium"
    else:
        return "confidence-low"

def predict_on_image(model, image):
    """Run detection on image"""
    img_array = np.array(image)
    results = model.predict(source=img_array, conf=0.25, device=0)
    return results

def draw_detections(image, results):
    """Draw detection results on image"""
    img = np.array(image)
    
    for result in results:
        boxes = result.boxes
        names = result.names
        
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            cls_name = names[cls]
            
            color = (0, 255, 0) if conf > 0.7 else (0, 165, 255) if conf > 0.5 else (0, 0, 255)
            cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
            
            label = f"{cls_name}: {conf:.2f}"
            cv2.putText(img, label, (x1, y1-10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
    return Image.fromarray(img)

def draw_detections_demo(image, detections):
    """Draw demo detections on image"""
    img = np.array(image)
    
    height, width = img.shape[:2]
    
    for i, (food_name, confidence) in enumerate(detections):
        box_height = height // (len(detections) + 1)
        y1 = (i + 1) * box_height - 20
        y2 = (i + 1) * box_height + 20
        x1 = 10
        x2 = width - 10
        
        color = (0, 255, 0) if confidence > 0.7 else (0, 165, 255) if confidence > 0.5 else (0, 0, 255)
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        
        label = f"{food_name}: {confidence:.2f}"
        cv2.putText(img, label, (x1 + 5, y1 + 20),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
    
    return Image.fromarray(img)

# Main app
st.markdown("# Food Detection and Health Information App")
st.markdown("---")

with st.sidebar:
    st.markdown("## Settings")
    confidence_threshold = st.slider(
        "Confidence Threshold",
        min_value=0.1,
        max_value=1.0,
        value=0.25,
        step=0.05,
        help="Minimum confidence for detection"
    )
    
    st.markdown("---")
    st.markdown("## Usage Guide")
    st.markdown("""
    1. Upload a food image (JPG, PNG, or WebP)
    2. Wait for detection results
    3. View confidence scores for each detection
    4. Read health benefits for detected foods
    
    Tips:
    - Use good lighting for best results
    - Food should be clearly visible
    - Take photos from normal angle (not tilted)
    """)
    
    st.markdown("---")
    if not YOLO_AVAILABLE:
        st.error("YOLOv8 not installed. App running in demo mode.")
    elif load_model() is None:
        st.warning("Trained model not found. App running in demo mode with color analysis.")
    else:
        st.info("Model: YOLOv8 Instance Segmentation")

col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown("### Upload Food Image")
    
    uploaded_file = st.file_uploader(
        "Select a food image",
        type=["jpg", "jpeg", "png", "webp"],
        help="Upload a food image for analysis"
    )
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded image", use_column_width=True)
        
        model = load_model()
        
        if model is not None:
            with st.spinner("Processing image..."):
                results = predict_on_image(model, image)
            detected_image = draw_detections(image, results)
            st.image(detected_image, caption="Detection results", use_column_width=True)
        else:
            with st.spinner("Analyzing image using color detection..."):
                detections = detect_food_from_image(image)
            detected_image = draw_detections_demo(image, detections)
            st.image(detected_image, caption="Detection results (demo mode)", use_column_width=True)
            
            st.markdown("""
            <div class="demo-mode">
            NOTE: Running in demo mode using color analysis. For better accuracy, please provide the trained YOLOv8 model.
            </div>
            """, unsafe_allow_html=True)

with col2:
    st.markdown("### Detection Results")
    
    if uploaded_file is not None:
        model = load_model()
        
        if model is not None:
            image = Image.open(uploaded_file)
            results = predict_on_image(model, image)
            
            detections = []
            for result in results:
                boxes = result.boxes
                names = result.names
                
                for box in boxes:
                    conf = float(box.conf[0])
                    cls = int(box.cls[0])
                    cls_name = names[cls]
                    
                    detections.append({
                        "name": cls_name,
                        "confidence": conf
                    })
        else:
            image = Image.open(uploaded_file)
            detections = []
            for food_name, confidence in detect_food_from_image(image):
                detections.append({
                    "name": food_name,
                    "confidence": confidence
                })
        
        if detections:
            detections = sorted(detections, key=lambda x: x['confidence'], reverse=True)
            
            st.markdown(f"**Total detections: {len(detections)} items**")
            
            for i, detection in enumerate(detections, 1):
                conf_color = get_confidence_color(detection['confidence'])
                st.markdown(f"""
                <div class="detection-result">
                <strong>{i}. {detection['name'].replace('_', ' ').title()}</strong><br>
                Confidence: <span class="{conf_color}">{detection['confidence']:.1%}</span>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No food items detected. Try uploading another image.")
    else:
        st.info("Upload an image to see detection results")

st.markdown("---")
st.markdown("### Health Benefits Information")

if uploaded_file is not None:
    model = load_model()
    
    if model is not None:
        image = Image.open(uploaded_file)
        results = predict_on_image(model, image)
        
        detections = []
        for result in results:
            boxes = result.boxes
            names = result.names
            
            for box in boxes:
                conf = float(box.conf[0])
                cls = int(box.cls[0])
                cls_name = names[cls]
                
                detections.append({
                    "name": cls_name,
                    "confidence": conf
                })
    else:
        image = Image.open(uploaded_file)
        detections = []
        for food_name, confidence in detect_food_from_image(image):
            detections.append({
                "name": food_name,
                "confidence": confidence
            })
    
    if detections:
        unique_foods = {}
        for detection in detections:
            food_name = detection['name'].lower()
            if food_name not in unique_foods or detection['confidence'] > unique_foods[food_name]:
                unique_foods[food_name] = detection['confidence']
        
        for food_name, confidence in unique_foods.items():
            benefit = get_food_benefit(food_name)
            
            st.markdown(f"""
            <div class="food-info">
            <h4>Food: {food_name.replace('_', ' ').title()}</h4>
            <p><strong>Benefits: </strong>{benefit}</p>
            <p><small>Confidence: {confidence:.1%}</small></p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Upload a food image to see health benefits information")
else:
    st.info("Upload an image above to see health benefits for detected foods")

st.markdown("---")
st.markdown("""
Food Detection App using YOLOv8 | Made for nutritional analysis
Dataset: UEC FOOD 100 | Model: YOLOv8 Instance Segmentation
""")
