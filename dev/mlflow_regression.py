import os
from pycaret.regression import *
from datetime import datetime


def main():
    df = pd.read_csv('../dev/data/insurance.csv')
    s = setup(df, target='charges',
              transform_target=True,
              log_experiment=True,
              experiment_name='cli_regression_insurance',
              session_id=123,
              silent=True, # -> run without action in background
              normalize=True,
              polynomial_features=True,
              trigonometry_features=True,
              feature_interaction=True,
              bin_numeric_features=['age', 'bmi'])

    best = compare_models()
    results = pull()

    # finalize the model
    final_best = finalize_model(best)  # save model to disk
    data_ref = datetime.today()
    month = '{:02d}'.format(data_ref.month)
    day = '{:02d}'.format(data_ref.day)
    year = '{:04d}'.format(data_ref.year)
    folder = f"{year}/{month}/{day}"
    in_file = f"out/{folder}/"
    os.makedirs(in_file, exist_ok=True)
    data_ref_file = data_ref.strftime('%Y-%m-%d %H:%M:%S')
    save_model(final_best, f'{in_file}cli_regression_insurance_{data_ref_file}')
    results.to_csv(f'{in_file}compare_models_{data_ref_file}.csv')

    create_api(final_best, f'{in_file}cli_regression_insurance_{data_ref_file}')


if __name__ == '__main__':
    print("===== START =====")
    main()
    print("===== END =====")
