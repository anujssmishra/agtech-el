# Glossary

| Term | Meaning in this project |
|---|---|
| **Agtech app** | A farmer-facing Android app offering advice, inputs, markets, finance or services |
| **AI launch** | The month an app made a farmer-facing AI feature available (photo diagnosis, chatbot, voice assistant, AI advisory) |
| **AI from launch** | An app that had AI from its first release; no before/after comparison possible, so excluded from the main estimate |
| **Treated app** | An app with a dated AI launch and `include = 1` |
| **Comparison app** | An app with no AI found and `include = 1`; it helps estimate the India-wide trends |
| **Check first** | An app whose AI status or package is still unresolved |
| **Sampling frame** | The workbook listing all candidate apps, exclusions, checks, launch log and firm events |
| **Package ID** | The app's unique Google Play identifier, for example `com.ulink.agrostar` |
| **Bucket** | One app × requested language stream in the scraper |
| **Romanized** | An Indian language written in Latin letters ("bahut accha app hai") |
| **Mixed review** | Mostly English with a few Indian-language words |
| **Native script** | Devanagari, Gujarati, Tamil and other Indian scripts |
| **IndicLID** | AI4Bharat's language identifier for 22 Indian languages (Madhani, Khapra and Kunchukuttan, ACL 2023) |
| **wordfreq** | Word-frequency lists used to recognise English words (Speer 2022) |
| **`n_main`, `n_mixed_ind`, `n_script`, `n_play`** | The four language measures (see `03_data.md`); `n_main` is the main one |
| **Indian-language share** | Indian-language reviews / (Indian + English reviews); undetermined and no-text reviews left out |
| **Panel** | The app × language × month table of review counts, zeros included |
| **`include`** | 1 if the app is in the estimation sample (in `launch_dates.csv`) |
| **`panel_end`** | Last month used for an app (shutdown, ownership change or abandoned app) |
| **PPML** | Poisson pseudo-maximum likelihood: a regression for counts that handles zeros (Santos Silva and Tenreyro 2006) |
| **Fixed effects** | Separate intercepts that absorb app × month, language × month and app × language differences |
| **β (beta)** | The coefficient on AI launch × Indian language; effect in % = 100 × (exp(β) − 1) |
| **Clustered SE** | Standard error allowing correlation within an app; too small in this design |
| **Randomization inference (RI)** | Re-estimating with launches given to random apps and months many times; the p-value is the share of placebo estimates at least as large as the real one |
| **Placebo draw** | One such re-estimate with fake launches |
| **Event study** | Effects by quarter before and after launch; checks for pre-trends and timing |
| **Pre-trend** | A difference that already exists before the launch; it would undermine the design |
| **Leave-one-out** | Re-estimating without each treated app in turn |
| **Overlap check** | Dropping treated apps with a funding round or acquisition within 3 months of the launch |
| **Staggered adoption** | Apps launch AI at different times; can bias simple estimators if effects differ across apps |
| **Power / detectable effect** | The smallest true effect the design would detect with 80% probability |
| **Cloud task** | An instruction file in `cloud_tasks/` that Claude Code on the web carries out |
| **Cowork** | The Claude chat linked to the author's own computer |
