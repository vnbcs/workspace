docker run --rm repronim/neurodocker:0.7.0 generate singularity \
    --base debian:stretch --pkg-manager apt --minc create_env=neuro \
    conda_install="python=3.9" pip_install="numpy pandas matplotlib \
    seaborn scipy nilearn nipype" 
