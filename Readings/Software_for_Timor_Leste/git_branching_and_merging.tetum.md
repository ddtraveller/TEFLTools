'Git Branching no Merging Workflow
Iha Git, branching mak dalan ida atu servisu iha versaun sira ne'ebé diferente husi repository iha tempu hanesan. Ne'e uza ona barak hodi dezenvolve funsionalidade (features), hadia erros (bugs) ka hamosu ideia foun sira nune'e la afeta versaun prinsipal husi projetu. Branching permite dezenvolvimentu iha tempu hanesan, ne'ebé dezenvolvedor sira bele halo servisu iha funsionalidade diferente sira iha tempu hanesan la interfere malu nia servisu.

Vokabulariu Xave:

Repository: Koleksaun husi dokumentu sira no sira nia istoria versaun.
Branch: Versaun ida husi repository ne'ebé la hanesan ho versaun prinsipal.
Merge: Hakat liu husi integra mudansa husi branch ida ba seluk.
Pedidu Pull (PR): Pedidu ida atu integra mudansa husi branch ida ba seluk, normalmente uza hodi revizaun kodigu no kolaborasaun.

Workflow ida ne'ebé normal:

Kria branch: Husi branch prinsipal (normalmente 'master' ka 'main'), kria branch foun ida ba ita nia funsionalidade ka hadia uza git branch <branch-foun>.
bashCopy# Kria branch foun 'feature-x' husi branch 'main'
git branch feature-x main

Troka ba branch foun: Uza git checkout <branch-foun> atu troka ita nia pasta servisu ba branch foun.
bashCopy# Troka ba branch 'feature-x'
git checkout feature-x

Halo mudansa no commit: Halo mudansa iha dokumentu, prepara mudansa, no halo commit iha ita nia branch foun hanesan deskreve iha Git Workflow.
bashCopy# Halo mudansa iha dokumentu
# Prepara mudansa
git add file1.txt file2.txt
# Commit mudansa
git commit -m "Implementa funsionalidade X"

Fó branch: Bainhira ita nia servisu iha branch prontu ona atu fo, fó branch ba repository remotu uza git push -u origin <branch-foun>.
bashCopy# Fó branch 'feature-x' ba repository remotu 'origin'
git push -u origin feature-x

Teste no revizaun: Iha ambiente kolaborativu, branch foun bele hetan teste, QA, no revizaun husi kolaborador sira uza ambiente pre-produksaun. Ne'e asegura katak mudansa foun sira tuir padraun ne'ebé presiza no la hamosu erros.

Kria pedidu Pull: Bainhira branch ona atu integra ba branch prinsipal, kria pedidu Pull (PR) iha GitHub (ka ekivalente iha sistema seluk). Ne'e aviza membru ekipa seluk no permite revizaun final. PR halo nudar plataforma ida ba diskusaun, feedback, no mudansa tan se presiza.

Merge branch: Hafoin PR hetan aprovasaun, bele integra branch ba branch prinsipal. Normalmente halo liu husi interface GitHub, ne'ebé halo hanesan git merge <branch-foun>. Integra mudansa husi branch funsionalidade ba branch prinsipal, halo sira parte husi versaun prinsipal husi projetu.

Rezolve konflitu merge: Iha kazu balun, integra branch bele hamosu konflitu merge bainhira parte hanesan husi dokumentu modifika ona iha branch funsionalidade no branch prinsipal. Presiza rezolve konflitu sira ne'e manualmente liu husi edita dokumentu sira ne'ebé afetadu, deside mudansa ne'ebé atu manten, no depois commit rezolusaun.

Hanoin branch: Hafoin integra branch no la presiza ona, bele hanoin branch lokál (git branch -d <branch-foun>) no iha remotu (git push origin --delete <branch-foun>). Ne'e manten repository hamoos no foka dezenvolvimentu iha branch prinsipal no funsionalidade branch sira seluk ne'ebé ativa.
bashCopy# Hanoin branch 'feature-x' iha lokál