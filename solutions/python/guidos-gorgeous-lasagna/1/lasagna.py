
# الثوابت المطلوبة
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """حساب الوقت المتبقي في الفرن."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """حساب وقت التحضير بناءً على عدد الطبقات."""
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """حساب الوقت الكلي المنقضي (تحضير + خبز)."""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time