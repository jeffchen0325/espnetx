import sys
from pathlib import Path
from TEMPLATE.asr.run import DEFAULT_STAGES, main
from espnet3.systems.asr.system import ASRSystem

if __name__ == "__main__":
    main(
        sys_args=sys.argv[1:],
        system_cls=ASRSystem,
        stages=DEFAULT_STAGES,
    )
