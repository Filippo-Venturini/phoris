from dataclasses import dataclass
import psutil
import subprocess

@dataclass
class HardwareProfile:
    ram_total_mb: int
    ram_available_mb: int
    has_gpu: bool
    vram_mb: int | None


def _detect_gpu() -> tuple[bool, int | None]:
    try:
        result = subprocess.run(
            ["nvidia-smi", "--query-gpu=memory.total", "--format=csv,noheader,nounits"],
            capture_output=True,
            text=True,
        )
        vram_mb = int(result.stdout.strip())
        return True, vram_mb
    except FileNotFoundError:
        return False, None


def detect() -> HardwareProfile:
    vmem = psutil.virtual_memory()
    has_gpu, vram_mb = _detect_gpu()
    return HardwareProfile(
        ram_total_mb=vmem.total // 1024 ** 2,
        ram_available_mb=vmem.available // 1024 ** 2,
        has_gpu=has_gpu,
        vram_mb=vram_mb,
    )