# Food Detection and Health Information Application

A Streamlit-based web application for detecting food items in images and providing health benefit information. The application can run in two modes: with a trained YOLOv8 model for accurate detection, or in demo mode using color analysis.

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation Steps

1. Navigate to the project directory:

```bash
cd fooSegmentation-master
```

2. Create and activate virtual environment:

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

### Running the Application

Start the application using the batch script (Windows):
```bash
run_app.bat
```

Or use the command line:
```bash
streamlit run app.py --server.port 8502
```

The application will open automatically at http://localhost:8502

## Features

### Image Upload

- Supports JPG, PNG, and WebP formats
- Drag-and-drop or click to browse interface

### Food Detection

- Two modes: Model-based detection and demo mode with color analysis
- Confidence scores for each detected item
- Visual bounding boxes on detected food items

### Health Benefits

- Database of 27 food types with health information
- Automatic lookup based on detected food items
- Displays nutritional benefits and recommendations

### Confidence Levels

- Green (>70%): High confidence detection
- Orange (50-70%): Medium confidence detection
- Red (<50%): Low confidence detection

## Application Modes

### Mode 1: With Trained Model (Recommended)
When the trained YOLOv8 model is available at `models/uecfoodpix_v1/weights/best.pt`, the application uses accurate instance segmentation for detection.

### Mode 2: Demo Mode
When the trained model is not available, the application automatically switches to demo mode using color-based analysis. While less accurate, it allows the application to function without the model file.

## Project Structure

```
fooSegmentation-master/
├── app.py                           # Main Streamlit application
├── requirements.txt                 # Python dependencies
├── run_app.bat                      # Windows batch script
├── models/
│   └── uecfoodpix_v1/
│       └── weights/
│           └── best.pt              # Trained model (if available)
├── data/                            # Dataset directory
├── notebook/                        # Jupyter notebooks
│   ├── preparation.ipynb            # Data preparation
│   ├── model-train.ipynb            # Model training
│   └── food.yaml                    # Dataset configuration
└── README.md                        # This file
```

## Using the Application

### Upload an Image

1. Click "Select a food image" button
2. Choose JPG, PNG, or WebP image file
3. Image preview appears immediately

### View Detection Results

- Detection results appear in the right panel
- Each detected item shows name and confidence percentage
- Visual representation with bounding boxes on the image

### Read Health Benefits

- Scroll down to see health benefits section
- Information includes nutritional content and recommendations
- Benefits are automatically matched to detected food items

## Troubleshooting

### Port Already in Use
If port 8502 is already in use, specify a different port:
```bash
streamlit run app.py --server.port 8503
```

### Model Not Found
The application automatically detects missing models and switches to demo mode. To use the trained model:

1. Train the model using notebook/model-train.ipynb
2. Ensure model is saved at models/uecfoodpix_v1/weights/best.pt

### Image Upload Issues

- Ensure image format is JPG, PNG, or WebP
- Keep image file size reasonable (< 10MB recommended)
- Verify image contains visible food items

### Application Crashes

1. Check that all dependencies are installed: `pip install -r requirements.txt`
2. Ensure Python version is 3.8 or higher
3. Try restarting the application

## Food Database

The application includes health benefit information for 27 food types:

- Basic items: Rice, Bread, Noodles, Pasta
- Proteins: Chicken, Beef, Fish, Egg, Tofu, Tempeh
- Vegetables and Fruits
- Dairy: Milk, Cheese
- Prepared dishes: Sushi, Curry, Soup, Ramen, Pizza, Burger, Sandwich
- Desserts: Cake, Donut

Each food item includes information about:

- Primary nutrients
- Health benefits
- Consumption recommendations

## System Requirements

### Minimum

- Python 3.8+
- 2GB RAM
- 500MB disk space

### Recommended

- Python 3.10+
- 4GB RAM
- 1GB disk space
- NVIDIA GPU with 6GB VRAM (for faster inference)

## Performance

### Without Model (Demo Mode)

- Processing time: <1 second per image
- CPU only
- Less accurate but functional

### With Trained Model

- Processing time: 0.5-1 second (GPU)
- Processing time: 2-5 seconds (CPU)
- More accurate detection

## Training Your Own Model

To train a new model:

1. Prepare dataset using notebook/preparation.ipynb
2. Run training using notebook/model-train.ipynb
3. Model will be saved to models/uecfoodpix_v1/weights/best.pt
4. Restart the application to use the new model

Estimated training time: 10-14 hours on NVIDIA RTX 4050

## Dependencies

- ultralytics: YOLOv8 implementation
- streamlit: Web interface framework
- opencv-python: Image processing
- torch & torchvision: Deep learning framework
- numpy: Numerical computing
- Pillow: Image handling

For complete list, see requirements.txt

## Common Issues and Solutions

### Issue: "WinError 10013" socket error
Solution: Use run_app.bat which automatically uses port 8502, or specify port manually

### Issue: Model takes long time to load
Solution: This is normal on first run. Subsequent runs are cached and faster

### Issue: Detection accuracy is low
Solution: 

- Ensure good lighting when taking photos
- Keep food clearly visible and centered
- Food items should not overlap significantly

### Issue: Application won't start
Solution:

1. Verify Python version: python --version
2. Reinstall dependencies: pip install --upgrade -r requirements.txt
3. Check that port 8502 is not in use
4. Restart computer if issues persist

## File Descriptions

### app.py
Main Streamlit application containing:

- UI layout and styling
- Model loading and caching
- Image processing functions
- Detection pipeline (both model-based and demo mode)
- Health benefits database and lookup

### run_app.bat
Windows batch script that:

- Activates virtual environment
- Runs app on port 8502
- Handles common port conflicts

### requirements.txt
Lists all Python package dependencies needed to run the application

### notebook/preparation.ipynb
Jupyter notebook for:

- Downloading UEC FOOD dataset
- Converting to YOLO format
- Data validation and statistics

### notebook/model-train.ipynb
Jupyter notebook for:

- Loading pre-trained YOLOv8 model
- Training on food dataset
- Evaluating model performance
- Saving trained model weights

## Resources

- Streamlit Documentation: https://docs.streamlit.io
- YOLOv8 Documentation: https://docs.ultralytics.com
- UEC FOOD Dataset: http://foodcam.mobi/dataset100.html
- PyTorch: https://pytorch.org

## Notes

- The application works without a trained model by using demo mode
- Color-based detection in demo mode provides reasonable accuracy for simple food categorization
- For production use, provide trained YOLOv8 model
- Application data is processed locally, not uploaded to servers
- Images are not saved after processing

## License

This project uses:

- YOLOv8 (AGPL-3.0)
- UEC FOOD Dataset (check original dataset terms)
- Streamlit (Apache 2.0)

## Version

Current Version: 1.0
Last Updated: 2024

Status: Production Ready
All features tested and working

## Installation

### 1. Clone or Navigate to Repository

```bash
cd fooSegmentation-master
```

### 2. Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Dependencies:**

- `ultralytics>=8.0.0` - YOLO implementation
- `opencv-python>=4.5.0` - Image processing
- `torch>=2.0.0` - Deep learning framework
- `torchvision>=0.15.0` - Computer vision utilities
- `numpy>=1.21.0` - Numerical computing
- `pandas>=1.3.0` - Data analysis
- `scikit-learn>=1.0.0` - Machine learning utilities
- `matplotlib>=3.4.0` - Visualization
- `tqdm>=4.60.0` - Progress bars
- `PyYAML>=5.4.0` - YAML configuration files
- `Pillow>=8.0.0` - Image processing

### 4. Verify GPU Setup (Optional)

```bash
python -c "import torch; cuda_avail = torch.cuda.is_available(); gpu_name = torch.cuda.get_device_name(0) if cuda_avail else 'None'; print(f'CUDA available: {cuda_avail}'); print(f'GPU: {gpu_name}')"
```

## Project Structure

```
fooSegmentation-master/
├── data/
│   ├── dataset_yolo/
│   │   ├── images/
│   │   │   ├── train/          # Training images
│   │   │   └── val/            # Validation images
│   │   └── labels/
│   │       ├── train/          # YOLO format labels (train)
│   │       └── val/            # YOLO format labels (val)
│   └── UECFOODPIX/             # Original UEC FOOD dataset
├── models/
│   └── uecfoodpix_v1/          # Trained models
├── notebook/
│   ├── preparation.ipynb       # Data preparation pipeline
│   ├── model-train.ipynb       # Training and evaluation
│   ├── food.yaml               # Dataset configuration
│   └── runs/                   # Training logs and outputs
├── requirements.txt
└── README.md
```

## Usage

### 1. Data Preparation

Open and run `notebook/preparation.ipynb` to:

- Download or prepare the UEC FOOD dataset
- Convert dataset to YOLO format
- Split into training/validation sets
- Generate data statistics

**Steps in preparation notebook:**

1. Import necessary libraries
2. Set up dataset paths
3. Create YOLO format dataset
4. Verify data integrity

### 2. Model Training

Open and run `notebook/model-train.ipynb` to:

- Load YOLOv8s-seg pretrained model
- Train on UEC FOOD dataset
- Monitor training progress
- Evaluate model performance

**Key Configuration (Optimized for RTX 4050 6GB VRAM):**

- Model: `yolov8s-seg.pt` (3.2M parameters)
- Epochs: 20 (better convergence with longer training)
- Batch Size: 4 (optimized for 6GB GPU VRAM)
- Image Size: 384x384 (balance for 6GB VRAM)
- Workers: 6 (optimal for 16GB RAM system)
- Cache: True (faster loading after first epoch)

**Training Parameters (Optimized for your setup):**

```python
results = model.train(
    data="food.yaml",          # Dataset configuration
    epochs=20,                 # 20 epochs for better convergence
    imgsz=384,                 # Reduced from 416 for 6GB VRAM
    batch=4,                   # Reduced for RTX 4050 stability
    workers=6,                 # Increased for 16GB RAM
    patience=10,               # Early stopping patience
    project="../runs/segment", # Output directory
    name=VERSION,              # Run name
    device=0,                  # GPU device ID
    amp=True,                  # Automatic Mixed Precision
    half=True,                 # FP16 precision for memory savings
    lr0=0.01,                  # Initial learning rate
    lrf=0.01,                  # Final learning rate
    cache=True,                # Cache images for faster loading
    flipud=0.3,                # Vertical flip augmentation
    fliplr=0.5,                # Horizontal flip augmentation
    mosaic=1.0,                # Mosaic data augmentation
    close_mosaic=5,            # Close mosaic at epoch 5
    augment=True,              # Enable data augmentation
)
```

**Expected Training Time:**

- Batch size 4 → ~30-40 min per epoch on RTX 4050
- Total training time: ~10-14 hours for 20 epochs
- Consider running overnight or in background

### 3. Model Evaluation

The evaluation cell in `model-train.ipynb` will:

- Load the best trained model
- Run validation on the validation set
- Display per-class metrics
- Calculate overall mAP scores

## Common Issues and Solutions

### Issue 1: "CUDA is not available"

**Solution:**

- Ensure NVIDIA GPU driver is installed: `nvidia-smi`
- Reinstall torch with CUDA: `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118`
- Use CPU mode: Add `device='cpu'` to training parameters

### Issue 2: "Out of memory" errors

**Solution for RTX 4050 (6GB VRAM):**

- Current settings (batch=4, imgsz=384) are optimized for your GPU
- If still getting OOM errors, try:
  - Reduce batch size: Change `batch=4` to `batch=2`
  - Reduce image size: Change `imgsz=384` to `imgsz=320`
  - Reduce workers: Change `workers=6` to `workers=2`
  - Disable cache: Change `cache=True` to `cache=False`
  - Close other GPU applications

### Issue 3: "No module named 'ultralytics'"

**Solution:**

- Ensure virtual environment is activated
- Reinstall requirements: `pip install -r requirements.txt --upgrade`

### Issue 4: "Data files not found"

**Solution:**

- Verify dataset is in `data/dataset_yolo/`
- Run data preparation notebook first
- Check paths in `food.yaml`

### Issue 5: Notebook kernel errors

**Solution:**

- Restart kernel: In Jupyter, use Kernel → Restart Kernel
- Ensure correct kernel selected: `.venv` (python3)
- Verify all imports work: Run first cell with imports

## Dataset Information

**UEC FOOD Dataset:**

- 102 food classes
- ~10,000 training images
- ~1,800 validation images
- Classes: rice, sushi, curry, noodles, bread, desserts, etc.

**Data Quality:**

- Some images may have been restored due to corruption
- Class imbalance: Some classes have limited samples
- Data augmentation applied during training

## Training Tips

1. **GPU Memory**: Start with batch_size=4 and increase if you have free VRAM
2. **Training Time**: ~2-4 hours on NVIDIA RTX 4050 for 10 epochs
3. **Early Stopping**: Training stops early if validation metric doesn't improve
4. **Checkpoints**: Models saved automatically at `runs/segment/<version>/weights/`
5. **Monitoring**: TensorBoard logs available in runs directory

## Model Performance

Expected metrics on validation set:

- **mAP50 (box)**: ~0.18-0.20
- **mAP50-95 (box)**: ~0.15-0.17
- **mAP50 (mask)**: ~0.18-0.20
- **mAP50-95 (mask)**: ~0.13-0.15

**Note:** Performance varies based on:

- Image quality and annotations
- Number of training epochs
- Data augmentation settings
- Class representation in dataset

## Hardware-Specific Optimization

### For RTX 4050 Laptop (6GB VRAM, 16GB RAM, Ryzen 7 8845HS)

**Current Optimized Settings:**

```
Configuration: batch=4, imgsz=384, workers=6
Estimated Training Time: 10-14 hours for 20 epochs
Memory Usage: ~5.5-6GB VRAM, ~8-10GB RAM
Per Epoch Time: 30-40 minutes
```

**If you need faster training (trade-off with accuracy):**

- Reduce epochs: 20 → 10
- Reduce image size: 384 → 320
- Reduce batch size: 4 → 3 (saves minimal time)
- Result: ~5-7 hours total

**If you want better accuracy (trade-off with time):**

- Increase epochs: 20 → 30 or 50
- Keep batch=4, imgsz=384
- Result: 15-35 hours total

**Memory Monitoring During Training:**

```bash
# Monitor GPU memory in another terminal
watch -n 1 nvidia-smi
```

**Performance Tips for Your Setup:**

1. Close unnecessary applications (especially browser, Discord, etc.)
2. Use Task Manager to ensure nothing else uses GPU
3. Monitor temperature: RTX 4050 should stay under 80°C
4. Training time can be reduced 30% by using smaller imgsz (320)
5. Consider running training in background: detach terminal or use screen/tmux

## Inference (Optional)

To use a trained model for inference:

```python
from ultralytics import YOLO

# Load model
model = YOLO('models/uecfoodpix_v1/weights/best.pt')

# Predict on image
results = model.predict(source='path/to/image.jpg', conf=0.25)

# Visualize
for r in results:
    print(r.boxes)  # Detection boxes
    print(r.masks)  # Segmentation masks
```

## File Descriptions

| File | Purpose |
|------|---------|
| `requirements.txt` | Python dependencies |
| `notebook/preparation.ipynb` | Data download and processing |
| `notebook/model-train.ipynb` | Model training and evaluation |
| `notebook/food.yaml` | Dataset configuration for YOLO |
| `models/uecfoodpix_v1/` | Saved model weights |
| `data/dataset_yolo/` | Processed dataset in YOLO format |

## Troubleshooting Checklist

- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] `pip install -r requirements.txt` completed successfully
- [ ] GPU drivers updated (if using CUDA)
- [ ] Dataset downloaded and in correct location
- [ ] `food.yaml` paths match your data structure
- [ ] Jupyter kernel set to `.venv`
- [ ] First notebook cell (imports) runs without errors

## Performance Notes

- **CPU Mode**: Training will be very slow (10+ hours)
- **GPU Mode**: Recommended for practical use
- **Batch Size Impact**: Larger batch sizes improve training stability but use more memory
- **Image Size Impact**: Larger images improve accuracy but increase computation time

## Next Steps for Improvement

1. **Collect More Data**: Especially for underrepresented classes
2. **Tune Hyperparameters**: Learning rate, augmentation, image size
3. **Increase Model Size**: Try YOLOv8m or YOLOv8l for better accuracy
4. **Ensemble Models**: Combine multiple models for better predictions
5. **Post-processing**: Add custom post-processing for specific use cases

## References

- YOLOv8 Documentation: <https://docs.ultralytics.com/>
- UEC FOOD Dataset: <http://foodcam.mobi/dataset100.html>
- PyTorch Documentation: <https://pytorch.org/docs/>

## License

This project uses:

- YOLOv8 (AGPL-3.0)
- UEC FOOD Dataset (check original dataset terms)

## Support

For issues or questions:

1. Check the Troubleshooting section above
2. Review Jupyter notebook comments
3. Check Ultralytics documentation
4. Verify all dependencies are correctly installed

---

**Last Updated:** 2024
**Python Version:** 3.8+
**PyTorch Version:** 2.0+
**CUDA Version:** 11.8+ (optional)
