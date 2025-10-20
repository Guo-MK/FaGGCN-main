from model.GCNpackage import run_gcn
import pandas as pd

config = {
        'seed': 658,
        'k_folds': 5,
        'adj_matrix_path': 'data/BRCA/GAE0.95_AfterGAE_for_try.csv',
        'sim_matrix_path': 'data/BRCA/SNF400_AfterSNF_for_try.csv',
        'features_path': 'data/BRCA/SURVIVE_SELECT_for_try.csv',
        'clinical_path': 'data/BRCA/down_clinical.csv',
        'dropout': 0.4,
        'lr': 0.05,
        'weight_decay': 0.001,
        'epochs': 500,
        'label_map': {'LumA': 0, 'LumB': 1, 'Basal': 2, 'Her2': 3},
        'label_column': 'PAM50Call_RNAseq'
    }
fold_performance, accuracies, precision, recall, f1 = run_gcn(config)
fold_performance_df = pd.DataFrame(fold_performance)

fold_performance_df.to_csv('data/BRCA/fold_performance5.csv', index=False)
performance_metrics_df = pd.DataFrame({
        'accuracies': [x[0] for x in accuracies],
        'precision': [x[0] for x in precision],
        'recall': [x[0] for x in recall],
        'f1': [x[0] for x in f1]
    })
performance_metrics_df.to_csv('data/BRCA/performance_metrics5.csv', index=False)