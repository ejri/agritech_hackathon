# Copyright 2020 The TensorFlow Authors. All Rights Reserved.
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
"""Model specification."""

import inspect

from tensorflow_examples.lite.model_maker.core.task.model_spec.image_spec import efficientnet_lite0_spec
from tensorflow_examples.lite.model_maker.core.task.model_spec.image_spec import efficientnet_lite1_spec
from tensorflow_examples.lite.model_maker.core.task.model_spec.image_spec import efficientnet_lite2_spec
from tensorflow_examples.lite.model_maker.core.task.model_spec.image_spec import efficientnet_lite3_spec
from tensorflow_examples.lite.model_maker.core.task.model_spec.image_spec import efficientnet_lite4_spec
from tensorflow_examples.lite.model_maker.core.task.model_spec.image_spec import ImageModelSpec
from tensorflow_examples.lite.model_maker.core.task.model_spec.image_spec import mobilenet_v2_spec
from tensorflow_examples.lite.model_maker.core.task.model_spec.image_spec import resnet_50_spec

from tensorflow_examples.lite.model_maker.core.task.model_spec.text_spec import average_word_vec_spec
from tensorflow_examples.lite.model_maker.core.task.model_spec.text_spec import AverageWordVecModelSpec
from tensorflow_examples.lite.model_maker.core.task.model_spec.text_spec import bert_classifier_spec
from tensorflow_examples.lite.model_maker.core.task.model_spec.text_spec import bert_qa_spec
from tensorflow_examples.lite.model_maker.core.task.model_spec.text_spec import bert_spec
from tensorflow_examples.lite.model_maker.core.task.model_spec.text_spec import BertClassifierModelSpec
from tensorflow_examples.lite.model_maker.core.task.model_spec.text_spec import BertModelSpec
from tensorflow_examples.lite.model_maker.core.task.model_spec.text_spec import BertQAModelSpec
from tensorflow_examples.lite.model_maker.core.task.model_spec.text_spec import mobilebert_classifier_spec
from tensorflow_examples.lite.model_maker.core.task.model_spec.text_spec import mobilebert_qa_spec
from tensorflow_examples.lite.model_maker.core.task.model_spec.text_spec import mobilebert_qa_squad_spec

# A dict for model specs to make it accessible by string key.
MODEL_SPECS = {
    'efficientnet_lite0': efficientnet_lite0_spec,
    'efficientnet_lite1': efficientnet_lite1_spec,
    'efficientnet_lite2': efficientnet_lite2_spec,
    'efficientnet_lite3': efficientnet_lite3_spec,
    'efficientnet_lite4': efficientnet_lite4_spec,
    'mobilenet_v2': mobilenet_v2_spec,
    'resnet_50': resnet_50_spec,
    'average_word_vec': average_word_vec_spec,
    'bert': bert_spec,
    'bert_classifier': bert_classifier_spec,
    'bert_qa': bert_qa_spec,
    'mobilebert_classifier': mobilebert_classifier_spec,
    'mobilebert_qa': mobilebert_qa_spec,
    'mobilebert_qa_squad': mobilebert_qa_squad_spec,
}

# List constants for supported models.
IMAGE_CLASSIFICATION_MODELS = [
    'efficientnet_lite0', 'efficientnet_lite1', 'efficientnet_lite2',
    'efficientnet_lite3', 'efficientnet_lite4', 'mobilenet_v2', 'resnet_50'
]
TEXT_CLASSIFICATION_MODELS = [
    'bert_classifier', 'average_word_vec', 'mobilebert_classifier'
]
QUESTION_ANSWERING_MODELS = ['bert_qa', 'mobilebert_qa', 'mobilebert_qa_squad']


def get(spec_or_str):
  """Gets model spec by name or instance, and initializes by default."""
  if isinstance(spec_or_str, str):
    model_spec = MODEL_SPECS[spec_or_str]
  else:
    model_spec = spec_or_str

  if inspect.isclass(model_spec) or inspect.isfunction(model_spec):
    return model_spec()
  else:
    return model_spec
