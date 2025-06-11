import random
from typing import List, Set, Dict

def sample_harmful_subsets(records: List[Dict], 
                         models: List[str], 
                         sample_size: int = 150) -> Set[str]:
    """
    Sample harmful subsets for each model where the model was wrong and others were right.
    
    Args:
        records: List of record dictionaries containing model predictions
        models: List of model names to analyze
        sample_size: Number of samples to collect per model's harmful subset
        
    Returns:
        Set of unique PIDs representing the combined harmful subsets
    """
    # Global set to store all sampled PIDs
    all_sampled_pids = set()
    
    for model1 in models:
        # For each model, find cases where it was wrong and at least one other model was right
        model1_harmful_cases = []
        
        for record in records:
            pid = record.get('pid')
            gt_label = record['output_label']
            model1_label = record.get(f'{model1}_output_label')
            
            # Check if model1 was wrong
            if not model1_label or model1_label == gt_label:
                continue
                
            # Check if any other model was right
            other_model_correct = False
            for model2 in models:
                if model2 == model1:
                    continue
                    
                model2_label = record.get(f'{model2}_output_label')
                if model2_label and model2_label == gt_label:
                    other_model_correct = True
                    break
            
            if other_model_correct:
                model1_harmful_cases.append(pid)
        
        # Sample from this model's harmful cases
        if model1_harmful_cases:
            sampled_pids = random.sample(
                model1_harmful_cases,
                min(sample_size, len(model1_harmful_cases))
            )
            all_sampled_pids.update(sampled_pids)
            print(f"{model1}: Found {len(model1_harmful_cases)} harmful cases, sampled {len(sampled_pids)}")
        else:
            print(f"{model1}: No harmful cases found")
    
    print(f"\nTotal unique PIDs in combined harmful subset: {len(all_sampled_pids)}")
    return all_sampled_pids

# Example usage:
"""
# Initialize your records and models list
records = [...]  # Your records data
models = ["model_a", "model_b", "model_c"]  # List of model names

# Get the sampled harmful subset
sampled_pids = sample_harmful_subsets(records, models)
""" 