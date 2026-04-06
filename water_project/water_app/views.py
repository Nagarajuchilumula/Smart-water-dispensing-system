from django.shortcuts import render, redirect
from .models import WaterOrder
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
import qrcode
from io import BytesIO
import base64

def home(request):
    return render(request, "home.html")

def create_order(request):
    if request.method == "POST":
        liters = int(request.POST.get("liters"))
        water_type = request.POST.get("water_type", "normal")

        if liters < 1 or liters > 100:
            return render(request, "order.html", {"error": "Enter 1-100 liters"})

        order = WaterOrder.objects.create(
            liters_requested=liters,
            water_type=water_type
        )

        return redirect(f"/pay/{order.id}/")

    return render(request, "order.html")


def payment_page(request, order_id):
    order = WaterOrder.objects.get(id=order_id)

    # ✅ STEP 2: Generate QR when user clicks "Generate QR"
    if request.method == "POST":
        upi_id = "9866884052-2@ybl"   # 🔁 replace with your UPI ID
        name = "Water Supply"
        amount = order.liters_requested

        upi_link = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR"

        qr = qrcode.make(upi_link)

        buffer = BytesIO()
        qr.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue()).decode()

        return render(request, "payment.html", {
            "order": order,
            "qr_code": img_str
        })

    # ✅ STEP 3: Default page load
    return render(request, "payment.html", {"order": order})


def success_page(request, order_id):
    """
    Success page after payment is confirmed
    """
    try:
        order = WaterOrder.objects.get(id=order_id)
        # Mark as paid when accessing success page
        if not order.is_paid:
            order.is_paid = True
            order.save()
        return render(request, "success.html", {"order": order})
    except WaterOrder.DoesNotExist:
        return redirect('/order/')


# API for Hardware
@api_view(['GET'])
def check_order(request, tap_id):
    order = WaterOrder.objects.filter(
        tap_id=tap_id,
        is_paid=True,
        is_dispensed=False
    ).first()

    if order:
        return Response({
            "order_id": order.id,
            "liters": order.liters_requested
        })

    return Response({"message": "No order"})


@api_view(['POST'])
def mark_dispensed(request, order_id):
    order = WaterOrder.objects.get(id=order_id)
    order.is_dispensed = True
    order.save()
    return Response({"status": "completed"})


@api_view(['GET'])
def check_payment_status(request, order_id):
    """
    API endpoint to check if payment is completed
    Returns JSON with payment status
    """
    try:
        order = WaterOrder.objects.get(id=order_id)
        if order.is_paid:
            return Response({"status": "paid"})
        return Response({"status": "pending"})
    except WaterOrder.DoesNotExist:
        return Response({"status": "error", "message": "Order not found"}, status=404)