#!/usr/bin/env python3
"""
Create an icon for DiffMatcher application
Generates a simple icon using Python's PIL (if available)
"""

def create_simple_icon():
    """Create a simple icon for the application"""
    try:
        from PIL import Image, ImageDraw, ImageFont
        icon_available = True
    except ImportError:
        icon_available = False
    
    if icon_available:
        # Create a 256x256 icon
        size = 256
        image = Image.new('RGBA', (size, size), (255, 255, 255, 0))
        draw = ImageDraw.Draw(image)
        
        # Background circle
        margin = 20
        draw.ellipse([margin, margin, size-margin, size-margin], 
                    fill=(70, 130, 180), outline=(25, 25, 112), width=8)
        
        # Draw comparison arrows
        center = size // 2
        arrow_color = (255, 255, 255)
        
        # Left arrow
        arrow1_points = [
            (center - 60, center - 20),
            (center - 20, center - 20),
            (center - 20, center - 40),
            (center + 10, center),
            (center - 20, center + 40),
            (center - 20, center + 20),
            (center - 60, center + 20)
        ]
        draw.polygon(arrow1_points, fill=arrow_color)
        
        # Right arrow
        arrow2_points = [
            (center + 60, center - 20),
            (center + 20, center - 20),
            (center + 20, center - 40),
            (center - 10, center),
            (center + 20, center + 40),
            (center + 20, center + 20),
            (center + 60, center + 20)
        ]
        draw.polygon(arrow2_points, fill=arrow_color)
        
        # Save as ICO file
        image.save('icon.ico', format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)])
        print("✅ Icon created: icon.ico")
        return True
    else:
        print("⚠️ PIL/Pillow not available. Creating placeholder icon...")
        # Create a simple text-based icon description
        with open("icon_instructions.txt", "w") as f:
            f.write("""Icon Instructions for DiffMatcher
=====================================

To add a custom icon to your executable:

1. Create or download a .ico file (256x256 pixels recommended)
2. Name it 'icon.ico' and place it in the same folder
3. Run the build_executable.py script

Suggested icon themes:
- Two documents with comparison arrows
- Magnifying glass over documents
- Side-by-side file comparison
- Diff/merge symbols

Free icon resources:
- https://icons8.com (search "file compare")
- https://www.flaticon.com (search "document compare")
- https://iconmonstr.com (search "file")

Or create your own using:
- GIMP (free)
- Paint.NET (free)
- Online icon generators
""")
        print("📄 Created icon_instructions.txt with guidance")
        return False

if __name__ == "__main__":
    print("🎨 Creating application icon...")
    if create_simple_icon():
        print("🎉 Icon creation completed!")
    else:
        print("📋 To add an icon, install Pillow: pip install Pillow")
