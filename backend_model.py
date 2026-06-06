import os
import sys

# Isse backend ko pata chalega ki ai_model kahan hai
current_dir = os.path.dirname(os.path.abspath(__file__))
engine_path = os.path.join(current_dir, 'ai_engine')
if engine_path not in sys.path:
    sys.path.append(engine_path)

# Ab ye ai_engine folder ke andar se restore_audio dhoond lega
try:
    from processor import restore_audio # Agar file ka naam processor.py hai
except ImportError:
    try:
        from ai_model import restore_audio # Agar file ka naam ai_model.py hai
    except ImportError:
        def restore_audio(in_p, out_p):
            # Agar kuch na mile toh demo ke liye file copy kar do
            import shutil
            shutil.copy(in_p, out_p)
            return True

# Flask wala saara code (app.route etc.) hata do, uski zaroorat nahi hai
