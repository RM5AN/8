
import os
import django
from decimal import Decimal

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shotspot.settings")
django.setup()

from store.models import Product

# حذف الكاميرات القديمة إذا كانت موجودة
old_cameras = [
    "كاميرا X-T30ll",
    "كاميرا كانون EOS R8",
    "كاميرا سوني Z6",
    "كاميرا كانون 5D Mark IV"
]

for name in old_cameras:
    Product.objects.filter(name=name).delete()
    print(f"🗑️ حذف المنتج القديم: {name}")

# قائمة المنتجات كاملة (18 منتج)
products = [
    {
        "name": "كاميرا X-T30ll",
        "description": "كاميرا عديمة المرآة بدقة 26 ميجابكسل وتصوير 4K.",
        "category": "cameras",
        "brand": "fujifilm",
        "price": 2580.0,
        "image": "Fujifilm-X-T30 (1).jpg",
        "is_for_rent": False,
        "is_for_sale": True
    },
    {
        "name": "كاميرا كانون EOS R8",
        "description": "كاميرا بدقة 30 ميجابكسل، تصوير 4K، شاشة LCD.",
        "category": "cameras",
        "brand": "canon",
        "price": 3250.0,
        "image": "4549292204889 R8 camera (1)-432x432.jpg",
        "is_for_rent": False,
        "is_for_sale": True
    },
    {
        "name": "كاميرا سوني Z6",
        "description": "كاميرا بدون مرآة بدقة 24 ميجابكسل، تصوير 4K.",
        "category": "cameras",
        "brand": "sony",
        "price": 980.0,
        "image": "4548736092440 sony camera (1)-432x432.jpg",
        "is_for_rent": False,
        "is_for_sale": True
    },
    {
        "name": "كاميرا كانون 5D Mark IV",
        "description": "كاميرا احترافية DSLR مناسبة للتصوير الفوتوغرافي والفيديو.",
        "category": "cameras",
        "brand": "canon",
        "price": 150.0,
        "image": "4549292204889 R8 camera (1)-432x432.jpg",
        "is_for_rent": True,
        "is_for_sale": False
    },
    {
        "name": "ميكروفون Rode VideoMic Pro+",
        "description": "ميكروفون احترافي لاتجاه الصوت مع بطارية قابلة للشحن وفلتر قطع التردد.",
        "category": "audio",
        "brand": "rode",
        "price": 1299.0,
        "image": "Rode VideoMic Pro (1).jpg",
        "is_for_rent": False,
        "is_for_sale": True
    },
    {
        "name": "حقيبة ظهر Lowepro ProTactic 450 AW II",
        "description": "حقيبة مقاومة للماء، تسع لكاميرات وعدسات ومجهزة للسفر.",
        "category": "bags",
        "brand": "lowepro",
        "price": 799.0,
        "image": "Lowepro ProTactic 450 AW II (1).jpg",
        "is_for_rent": False,
        "is_for_sale": True
    },
    {
        "name": "فلتر Hoya UV",
        "description": "فلتر مقاس 77mm مضاد للخدش للحماية من الأشعة فوق البنفسجية.",
        "category": "accessories",
        "brand": "hoya",
        "price": 199.0,
        "image": "Filter,K&F Concept 77mm (1).jpg",
        "is_for_rent": False,
        "is_for_sale": True
    },
    {
        "name": "عدسة كانون مايكرو",
        "description": "عدسة بفتحة f/1.8 وبُعد بؤري 24mm وتكبير 1:1.",
        "category": "lenses",
        "brand": "canon",
        "price": 2000.0,
        "image": "canon RF24mm (1).jpg",
        "is_for_rent": False,
        "is_for_sale": True
    },
    {
        "name": "كرت ذاكرة SanDisk Extreme Pro",
        "description": "ذاكرة 128GB بسرعة 170MB/s، مقاومة للماء.",
        "category": "accessories",
        "brand": "sandisk",
        "price": 299.0,
        "image": "SanDisk 128 (1).jpg",
        "is_for_rent": False,
        "is_for_sale": True
    },
    {
        "name": "بطارية Godox WB87",
        "description": "بطارية احترافية بسعة 8700mAh وشحن سريع.",
        "category": "accessories",
        "brand": "godox",
        "price": 349.0,
        "image": "Godox WB87 (1).jpg",
        "is_for_rent": False,
        "is_for_sale": True
    },
    {
        "name": "سماعات Beyerdynamic DT 770 Pro",
        "description": "سماعة استوديو مغلقة تعزل الضوضاء وتوفر دقة عالية.",
        "category": "audio",
        "brand": "beyerdynamic",
        "price": 999.0,
        "image": "Beyerdynamic DT 770 Pro (1).jpg",
        "is_for_rent": False,
        "is_for_sale": True
    },
    {
        "name": "عدسة كانون RF24-105mm",
        "description": "عدسة بفتحة f/1.8 وبُعد 50mm مقاومة للغبار والماء.",
        "category": "lenses",
        "brand": "canon",
        "price": 1348.0,
        "image": "canon RF24-105mm (1).jpg",
        "is_for_rent": False,
        "is_for_sale": True
    },
    {
        "name": "حقيبة حماية Think Tank Airport Security V3.0",
        "description": "حقيبة مقاومة للصدمات ومناسبة للسفر الجوي بقفل TSA.",
        "category": "bags",
        "brand": "think-tank",
        "price": 1399.0,
        "image": "Think Tank Airport Security V3.0 (1).jpg",
        "is_for_rent": False,
        "is_for_sale": True
    },
    {
        "name": "مسجل صوت Zoom H5 Handy Recorder",
        "description": "جهاز تسجيل احترافي بميكروفونات متعددة وتسجيل 15 ساعة.",
        "category": "audio",
        "brand": "zoom",
        "price": 1599.0,
        "image": "Zoom H5 Handy Recorder (1).jpg",
        "is_for_rent": False,
        "is_for_sale": True
    },
    {
        "name": "حقيبة كتف Peak Design Everyday Sling 10L",
        "description": "حقيبة خفيفة بسعة 10 لتر وتصميم مقاوم للسرقة.",
        "category": "bags",
        "brand": "peak-design",
        "price": 679.0,
        "image": "Peak Design Everyday Sling 10L (1).jpg",
        "is_for_rent": False,
        "is_for_sale": True
    },
    {
        "name": "عدسة Sigma 35mm f/1.4 Art",
        "description": "عدسة احترافية ببعد بؤري 35mm وفتحة f/1.4.",
        "category": "lenses",
        "brand": "sigma",
        "price": 2850.0,
        "image": "Sigma 35mm (1).jpg",
        "is_for_rent": False,
        "is_for_sale": True
    },
    {
        "name": "فلاش Godox V1",
        "description": "فلاش دائري قابل للتدوير، قوة 76 واط، TTL و HSS.",
        "category": "lighting",
        "brand": "godox",
        "price": 899.0,
        "image": "Godox V1 (1).jpg",
        "is_for_rent": False,
        "is_for_sale": True
    },
    {
        "name": "عكاسة Neewer 5 in 1",
        "description": "عكاسة متعددة الاستخدامات بحجم 110 سم لتعديل الإضاءة.",
        "category": "lighting",
        "brand": "neewer",
        "price": 149.0,
        "image": "Neewer 5 in 1 (1).jpg",
        "is_for_rent": False,
        "is_for_sale": True
    },
    {
        "name": "عدسة تامرون 70-180mm",
        "description": "عدسة تقريب ممتازة مع فتحة واسعة f/2.8.",
        "category": "lenses",
        "brand": "tamron",
        "price": 3199.0,
        "image": "Tamron 70-180mm (1).jpg",
        "is_for_rent": False,
        "is_for_sale": True
    }
]

added = 0
for item in products:
    if not Product.objects.filter(name=item["name"]).exists():
        Product.objects.create(
            name=item["name"],
            description=item["description"],
            category=item["category"],
            brand=item["brand"],
            price=Decimal(item["price"]),
            is_available=True,
            is_for_rent=item["is_for_rent"],
            is_for_sale=item["is_for_sale"],
            image=item["image"]
        )
        added += 1

print(f"✅ تمت إضافة {added} منتجاً إلى قاعدة البيانات.")
