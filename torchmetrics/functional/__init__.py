# Copyright The PyTorch Lightning team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from torchmetrics.functional.average_precision import average_precision  # noqa: F401
from torchmetrics.functional.classification import (  # noqa: F401
    accuracy,
    auc,
    auroc,
    dice_score,
    f1_score,
    fbeta_score,
    get_num_classes,
    iou,
    multiclass_auroc,
    precision,
    precision_recall,
    recall,
    stat_scores,
    stat_scores_multiple_classes,
    to_categorical,
    to_onehot,
)
from torchmetrics.functional.confusion_matrix import confusion_matrix  # noqa: F401

# TODO: unify metrics between class and functional, add below
from torchmetrics.functional.explained_variance import explained_variance  # noqa: F401
from torchmetrics.functional.f_beta import f1, fbeta  # noqa: F401
from torchmetrics.functional.mean_absolute_error import mean_absolute_error  # noqa: F401
from torchmetrics.functional.mean_squared_error import mean_squared_error  # noqa: F401
from torchmetrics.functional.mean_squared_log_error import mean_squared_log_error  # noqa: F401
from torchmetrics.functional.nlp import bleu_score  # noqa: F401
from torchmetrics.functional.precision_recall_curve import precision_recall_curve  # noqa: F401
from torchmetrics.functional.psnr import psnr  # noqa: F401
from torchmetrics.functional.roc import roc  # noqa: F401
from torchmetrics.functional.self_supervised import embedding_similarity  # noqa: F401
from torchmetrics.functional.ssim import ssim  # noqa: F401