// ===== PENGATURAN LINGUALENS =====
// URL workflow dan API key sekarang diisi di server.py (bukan di sini),
// supaya key tidak terlihat di browser.
const CONFIG = {
  MIN_CONFIDENCE: 0.6,   // objek di bawah 60% keyakinan diabaikan
  STABLE_FRAMES: 2,      // objek harus terdeteksi N kali berturut-turut
  COOLDOWN_MS: 4000,     // jeda sebelum kata yang sama diucapkan lagi
  INTERVAL_MS: 1200      // jeda antar kirim frame (hemat kredit Roboflow)
};