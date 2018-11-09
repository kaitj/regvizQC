from nipype.interfaces.base import (BaseInterface, BaseInterfaceInputSpec,
                                    traits, File, TraitedSpec, Directory)
from nipype.utils.filemanip import split_filename
from niworkflows.viz.utils import (cuts_from_bbox, compose_view,
                                   plot_registration)
from nilearn.image import load_img

import os

class RegistrationImageInputSpec(BaseInterfaceInputSpec):
    fixed_img = File(desc='Fixed image')
    moving_img = File(desc='Moving image')
    mask_img = File(desc='Mask of interest')
    out_dir = Directory(desc='output directory')
    cuts = traits.Int(default_value=7)

class RegistrationImageOutputSpec(TraitedSpec):
    out_svg = File(desc='Ouptut svg')

class RegistrationInterface(BaseInterface):
    input_spec = RegistrationImageInputSpec
    output_spec = RegistrationImageOutputSpec

    def _run_interface(self, runtime):
        fixed_img = load_img(self.inputs.fixed_img)
        moving_img = load_img(self.inputs.moving_img)
        mask = load_img(self.inputs.mask_img)
        out_dir = os.path.realpath(self.inputs.out_dir)
        cuts = cuts_from_bbox(mask, self.inputs.cuts)

        _, fname, _ = split_filename(self.inputs.moving_img)

        compose_view(plot_registration(fixed_img, 'fixed-image',
                                       estimate_brightness=True,
                                       cuts=cuts, label='fixed'),
                     plot_registration(moving_img, 'moving-image',
                                       estimate_brightness=True,
                                       cuts=cuts, label='moving'),
                     out_file=os.path.join(out_dir, (fname + '_vizQC.svg')))

        return runtime

    def _list_outputs(self):
        outputs = self._outputs().get()

        _, fname, _ = split_filename(self.inputs.moving_img)
        outputs["out_svg"] = os.path.join(os.path.realpath(self.inputs.out_dir),
                                (fname + '_vizQC.svg'))
        return outputs
