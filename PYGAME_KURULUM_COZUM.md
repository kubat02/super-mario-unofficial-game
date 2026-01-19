# 🔧 Pygame Kurulum Sorunu - Çözümler

## ❌ Sorun
Python ve pip kurulumunuz bozuk görünüyor. Pygame kurulumu yapılamıyor.

## ✅ Çözümler (Sırayla Deneyin)

### Çözüm 1: Python'u Yeniden Kurun (ÖNERİLEN)
1. **Python'u tamamen kaldırın:**
   - Ayarlar → Uygulamalar → Python 3.12
   - Kaldır düğmesine tıklayın

2. **Python'u yeniden kurun:**
   - https://www.python.org/downloads/ adresine gidin
   - "Download Python 3.12" düğmesine tıklayın
   - İndirilen dosyayı çalıştırın
   - ⚠️ **ÖNEMLİ**: "Add Python to PATH" kutucuğunu işaretleyin!
   - "Install Now" seçeneğini seçin

3. **Pygame'i kurun:**
   ```powershell
   python -m pip install pygame
   ```

4. **Oyunu çalıştırın:**
   ```powershell
   cd "c:\Users\KUBATB\Desktop\Yeni klasör (2)-20260118T232318Z-1-001\Yeni klasör (2)"
   python main.py
   ```

---

### Çözüm 2: Microsoft Store'dan Python Kurun
1. Microsoft Store'u açın
2. "Python 3.12" aratın
3. Python 3.12'yi yükleyin
4. Terminal'de:
   ```powershell
   python -m pip install pygame
   python main.py
   ```

---

### Çözüm 3: Pygame Wheel Dosyasını Manuel İndirin
1. https://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame adresine gidin
2. Python sürümünüze uygun pygame wheel dosyasını indirin:
   - `pygame-2.5.2-cp312-cp312-win_amd64.whl` (Python 3.12, 64-bit için)

3. İndirdiğiniz klasörde terminal açın ve:
   ```powershell
   python -m pip install pygame-2.5.2-cp312-cp312-win_amd64.whl
   ```

---

### Çözüm 4: Anaconda/Miniconda Kullanın
1. https://www.anaconda.com/download adresinden Anaconda'yı indirin
2. Kurun
3. Anaconda Prompt'u açın:
   ```bash
   conda create -n mario python=3.12
   conda activate mario
   conda install pygame
   cd "c:\Users\KUBATB\Desktop\Yeni klasör (2)-20260118T232318Z-1-001\Yeni klasör (2)"
   python main.py
   ```

---

## 🎮 Oyun Gereksinimleri
- **Python**: 3.8 veya üzeri
- **Pygame**: 2.0.0 veya üzeri

## 📦 Requirements.txt
Pygame kurulumu başarılı olunca:
```bash
pip install -r requirements.txt
```

## ❓ Hala Sorun Mu Var?

### Pygame'in kurulu olup olmadığını kontrol edin:
```powershell
python -c "import pygame; print(pygame.version.ver)"
```

Bu komut pygame sürümünü gösterirse, kurulum başarılı demektir!

---

## 🚀 Kısa Yol - Eğer Pygame Zaten Varsa
Belki başka bir Python kurulumunda pygame vardır. Kontrol edin:

```powershell
# Tüm Python kurulumlarını listele
where python

# Her birini test et
C:\Python39\python.exe -m pygame.examples.aliens
C:\Python310\python.exe -m pygame.examples.aliens
C:\Python311\python.exe -m pygame.examples.aliens
```

Çalışan birini bulursanız, o Python ile oyunu çalıştırın:
```powershell
C:\Python310\python.exe main.py
```

---

## 💡 Not
Mevcut Python kurulumunuz (`C:\Python312`) bozuk görünüyor. En iyi çözüm Python'u yeniden kurmaktır.
