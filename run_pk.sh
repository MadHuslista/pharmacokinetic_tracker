
#! /bin/bash

REPO_DIR="/home/zima/Documents/Outside_Life/Salud/TDAH/Simulation/flask_web/"
CLI_EXE=$REPO_DIR/pk/main.py
VENV_DIR=$REPO_DIR/.venv

# LDX PK PARAMETERS
HL="10"
TMAX="4.6"
DOSE="1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1"
OFFSETS="0 19 26 98 109 143 158 176 211 246.6 284 298.5 320.5 380 421.5 440.5 581.3 602.4 622.5 644.2 667.77 695.84 719.01 787.5 813.62 837.5 864.34 884.83 900 938.39 962.84 984.92 1003.97 1019.47 1112.0 1123.59 1140.79 1161.55 1218.9 1231.48 1243.15 1294.75 1307.24 1326.76 1345.92 1358.03 1377.9 1394.82 1418.20 1466.9 1477.33 1499.97 1513.71 1541.91 1555.72 1569.78 1637.78 1650.07 1666.25 1679.33 1701.08 1717 1734.17 1762.6 1777.17 1799 1820.92 1835.67 1854.17 1871.33 1896.14 1916.33 1943.17 1956.17"
DURATION="2000"


EXE="python ${CLI_EXE} --hl ${HL} --tmax ${TMAX} --dose ${DOSE}  --offsets ${OFFSETS} --duration ${DURATION}"

run_exe(){
    echo "Accessing Pk App.."
    # Run formatter  
    $EXE "$@"
}

# Check if the Python environment is activated
if [[ "$VIRTUAL_ENV" == "" ]]; then
    if [ -d "$VENV_DIR" ]; then
        . $VENV_DIR/bin/activate
        echo "Activated virtual environment.."
        cd $REPO_DIR
        run_exe "$@"
    else 
        echo "Virtual environment not found."
        exit 1
    fi

else
    echo "Virtual environment already activated."
fi

 
