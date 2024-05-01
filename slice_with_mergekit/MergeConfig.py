import sys

MODEL_ID = sys.argv[0]
final = int(sys.argv[1])
dtype = sys.argv[2]
l_0 = int(sys.argv[3])
l_n = int(sys.argv[4])

yaml_config = f"""
slices:
  - sources:
      - model: {MODEL_ID}
        layer_range: [0, {l_0-1}]
  - sources:
      - model: {MODEL_ID}
        layer_range: [{l_n}, {final}]
            
merge_method: passthrough
dtype: {dtype}
"""
# Save config as yaml file
with open('slice.yaml', 'w', encoding="utf-8") as f:
    f.write(yaml_config)