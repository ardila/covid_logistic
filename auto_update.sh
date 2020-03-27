cd ~/src/covid_logistic
python3 update_plots.py
git pull
git commit -a -m "auto update $(now)"
git push

