# regvizQC

regvizQC, a visual assessment tool for registration (based on fmriprep's QC)

## Contents
* [Usage](#usage)
    * [Required arguments](#reqarg)
    * [Optional arguments](#optarg)
* [Acknowledgements](#acknowledgment)

## Usage <a name="usage"></a>
`regvizQC [-h] [-v] [-c CUTS] [-o OUT_DIR] [-w WORK_DIR] fixed_img moving_img mask`

### Required arguments <a name="reqarg"></a>
```
fixed_img       Fixed image
moving_img      Moving image
mask            Mask over area of interest
```

### Optional arguments <a name="optarg"></a>
```
-c, --cuts      Number of images to visualize for each plane
-o, --out_dir   Output directory
-w, --work_dir  Working directory
-h, --help      Displays help message
-v, --version   Display program version
```

## Acknowledgments <a name="acknowledgement"></a>
Thanks to [O. Stanley](https://github.com/ostanley) for providing relevant code.
