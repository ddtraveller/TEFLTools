'# Afina Modelu Lian ho Kódigu Abertu liu husi WebUI

Afina perimite ita atu personaliza modelu ne'ebé sai tiha ona iha ita nia dataset espesífiku, bele hadi'a nia desempenhu ba ita nia kazu espesifikua. Iha ne'e mak guia pasu husi pasu atu afina ita nia modelu liuhusi WebUI:

## Pré-requisitu

- Haksegurá ita iha instala ona WebUI no karga modelu baze hanesan halo iha guia instalasaun anterior.
- Prepara ita-nia dataset ba afina (detalhus liu iha okos).

## Pasu atu Afina

1. **Prepara Ita-nia Dataset**
   - Kria dokumentu testu ho ita-nia dadus treinamentu.
   - Formata kada ezemplu hanesan konversa ka instrusaun-resposta par.
   - Ruma ne'e iha `training/datasets` pasta husi ita-nia instalasaun WebUI.

2. **Aksesa Tab Treinamentu**
   - Iha interface WebUI, buka tab "Treinamentu".

3. **Hili Ita-nia Dataset**
   - Iha seisaun "Dataset", hili ita-nia dataset ne'ebé prepara ona husi menu dropdown.

4. **Configura Parámetru Treinamentu**
   - Defini númeru de épokas (hira dala ita atu repete dataset).
   - Ajusta taxa aprendizajen (valor ki'ik hanesan 1e-5 ka 5e-5).
   - Defini tamañu lote (depende ba ita nia memória GPU, hahu ki'ik se la hatene).
   - Hili parámetru seluk hanesan pasu akumulasaun gradiente, pasu aklimatasaun, etc.

5. **Hili Métodu Treinamentu**
   - Hili entre afina total ka LoRA (Adaptasaun Ranku Kraik).
   - LoRA iha preferénsia tanba nia efisiente liu iha memória no la'o liu.

6. **Hahu Treinamentu**
   - Klik iha botun "Hahu Treinamentu" atu hahu prosesu afina.
   - Monitoriza progresu treinamentu iha saída konsola.

7. **Avalia Modelu ne'ebé Afina ona**
   - Hafoin treinamentu hotu, karga modelu ne'ebé afina ona iha interface prinsipál.
   - Testa ho instrusaun sira ne'ebé relasiona ho ita nia kazu espesífiku atu avalia desempenhu.

## Tips ba Afina Efektivu

1. **Kualidade Dadus**: Haksegurá ita nia dataset iha kualidade aas no reprezenta ita nia tarefa alvu.

2. **Kuantidade Dadus**: Dadus barak liu iha tendénsia atu hetan rezultadu di'ak, maibé duni ezemplu ruma resin liu atu bele benefisia.

3. **Tuning Hiperparámetru**: Eksperimenta ho taxa aprendizajen, tamañu lote, no épokas diferentes atu hetan konfigurasaun optimal.

4. **Evita Overfitting**: Monitoriza perda treinamentu no validasaun. Se perda validasaun aumenta, ita bele overfitting.

5. **Hahu Ki'ik**: Hahu ho modelu ka dataset ki'ik hodi familia ho prosesu antes aumenta.

6. **Afina Incremental**: Konsidera atu afina iha fase, hahu ho dataset jerál antes ba ita-nia kazu espesífiku.

7. **Kontrolu Versaun**: Mantein registo husi versaun sira husi ita nia modelu ne'ebé afina ona no sira nia dataset no parámetru korrespondente.

## Desafiu Potensial

- **Limitasaun Hardware**: Afina bele presiza rekursu barak. Se ita hasoru eror falta memória, tenta redús tamañu lote ka uza LoRA.