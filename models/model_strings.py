import warnings
import os

FILES = {}

assert os.path.exists("circ_models2"), "Where are the models???"

# get all files in the circ_models2 directory
for root, dirs, files in os.walk('circ_models2'):
  # if file isn't a .circ file, skip it
  for file in files:
    if file.endswith('.circ'):
      # add the file to the list of files
      FILES[str(file)] = os.path.join(root, file)
    else:
      warnings.warn("Found a file called " + str(file) + ": this doesn't seem right")

for fname, fpath in FILES.items():
  with open(fpath, 'r') as f:
    model_text = f.read()
    #  FILES[fname] = f.read()
  exec(f"{(fname[:-5]).replace('-', '_')}_string = model_text")

# print(FILES)

# gpt2_small = """# info:{"params": {"block_params": {"norm_type": "ln", "attn_bias": true, "attn_pos": false, "use_mlp": true, "mlp_act_type": "gelu", "mlp_output_bias": true}, "num_layers": 12, "use_norm_output": true, "output_bias": false}, "model_class": "GPT", "pos_enc_type": "gpt", "causal_mask": true, "extra": null}
# 't.w.tok_embeds' [50257,768] Array 1f668798fb95d0e16b2a0143
# 't.w.pos_embeds' [1024,768] Array 71f9b465008914ba28cdba38
# 't.bind_w' Module
#   't.logits'
#   'a0.ln.w.bias_arr' [768] Array b8bd8a90d0db28aa0302de9a ! 'a0.ln.w.bias' [0s] Symbol 8d723104-f773-83c1-3458-a748e9bb17bc
#   'a0.ln.w.scale_arr' [768] Array 243969425a9334c478301b1c ! 'a0.ln.w.scale' [0s] Symbol 85776e9a-dd84-f39e-7154-5a137a1d5006
#   'a0.w.q_arr' [12,64,768] Array 9f6ad6af4526a12cc44d2838 ! 'a0.w.q' [4s,7s,0s] Symbol 1846d424-c17c-6279-23c6-612f48268673
#   'a0.w.k_arr' [12,64,768] Array 5d4410f46dbd1d1452ddfa4b ! 'a0.w.k' [4s,7s,0s] Symbol b4862b21-fb97-d435-8856-1712e8e5216a
#   'a0.w.v_arr' [12,64,768] Array be3a40d0b97769f7f18e96ce ! 'a0.w.v' [4s,8s,0s] Symbol 12e0c8b2-bad6-40fb-1948-8dec4f65d4d9
#   'a0.w.o_arr' [12,768,64] Array ad7282377b6c9eb52bbbed20 ! 'a0.w.o' [4s,0s,8s] Symbol 5a921187-19c7-8df4-8f4f-f31e78de5857
#   'a0.w.q_bias_arr' [12,64] Array 703fa86711f4769810c5a6a6 ! 'a0.w.q_bias' [4s,7s] Symbol fcbd04c3-4021-2ef7-cca5-a5a19e4d6e3c
#   'a0.w.k_bias_arr' [12,64] Array 3a44ee2fa4c2d5b11da33c29 ! 'a0.w.k_bias' [4s,7s] Symbol 259f4329-e6f4-590b-9a16-4106cf6a659e
#   'a0.w.v_bias_arr' [12,64] Array 2b06e681e6c1171295f014cd ! 'a0.w.v_bias' [4s,8s] Symbol 5487ce1e-af19-922a-d9b8-a714e61a441c
#   'a0.w.o_bias_arr' [768] Array c6d8301380189e1b9bdb6b46 ! 'a0.w.o_bias' [0s] Symbol a3f2c9bf-9c63-16b9-50f2-44556f25e2a2
#   'm0.ln.w.bias_arr' [768] Array c09a18d23a5c16d077c80161 ! 'm0.ln.w.bias' [0s] Symbol e443df78-9558-867f-5ba9-1faf7a024204
#   'm0.ln.w.scale_arr' [768] Array 34fa95b940a136416a6e9219 ! 'm0.ln.w.scale' [0s] Symbol 23a7711a-8133-2876-37eb-dcd9e87a1613
#   'm0.w.proj_in_arr' [3072,768] Array e0118cea10d34268dc3679c0 ! 'm0.w.proj_in' [5s,0s] Symbol e3e70682-c209-4cac-629f-6fbed82c07cd
#   'm0.w.in_bias_arr' [3072] Array f58f9277ab22159514944405 ! 'm0.w.in_bias' [5s] Symbol f728b4fa-4248-5e3a-0a5d-2f346baa9455
#   'm0.w.proj_out_arr' [768,3072] Array 1abd3250105101978e11364d ! 'm0.w.proj_out' [0s,5s] Symbol eb1167b3-67a9-c378-7c65-c1e582e2e662
#   'm0.w.out_bias_arr' [768] Array f0f95228ce9514bc1519effb ! 'm0.w.out_bias' [0s] Symbol f7c1bd87-4da5-e709-d471-3d60c8a70639
#   'a1.ln.w.bias_arr' [768] Array 4401273331a64f1427708c96 ! 'a1.ln.w.bias' [0s] Symbol 8d88348a-7eed-8d14-f06d-3fef701966a0
#   'a1.ln.w.scale_arr' [768] Array 36034415540cb05da0f1e6ef ! 'a1.ln.w.scale' [0s] Symbol ad45f23d-3b1a-11df-587f-d2803bab6c39
#   'a1.w.q_arr' [12,64,768] Array b38a3866cc416be09171e17d ! 'a1.w.q' [4s,7s,0s] Symbol b2221a58-008a-05a6-c464-7159c324c985
#   'a1.w.k_arr' [12,64,768] Array febf65f5b5df27f04074cb00 ! 'a1.w.k' [4s,7s,0s] Symbol 1a2b8f1f-f1fd-42a2-9755-d4c13a902931
#   'a1.w.v_arr' [12,64,768] Array c409c61290454fbaa9dca080 ! 'a1.w.v' [4s,8s,0s] Symbol 025b413f-8a9a-021e-a648-a7dd06839eb9
#   'a1.w.o_arr' [12,768,64] Array 6bc6eee091efa8d72e611665 ! 'a1.w.o' [4s,0s,8s] Symbol b9d179e0-6c0f-d4f5-f813-0c4237730edf
#   'a1.w.q_bias_arr' [12,64] Array 493549a05e19b327ab254879 ! 'a1.w.q_bias' [4s,7s] Symbol cd447e35-b8b6-d8fe-442e-3d437204e52d
#   'a1.w.k_bias_arr' [12,64] Array 21da17b902ac8620662d6210 ! 'a1.w.k_bias' [4s,7s] Symbol 05b6e6e3-07d4-bedc-5143-1193e6c3f339
#   'a1.w.v_bias_arr' [12,64] Array 01cc3e825579c9d8a8b2de80 ! 'a1.w.v_bias' [4s,8s] Symbol afbd67f9-6196-99cf-e198-8ad9f06c144a
#   'a1.w.o_bias_arr' [768] Array 35d279f23c436901c8fd859f ! 'a1.w.o_bias' [0s] Symbol c381e88f-38c0-c8fd-8712-b8bc076f3787
#   'm1.ln.w.bias_arr' [768] Array a4e221a6903280b56efaa436 ! 'm1.ln.w.bias' [0s] Symbol e4b06ce6-0741-c7a8-7ce4-2c8218072e8c
#   'm1.ln.w.scale_arr' [768] Array b4c2ad28b0d6a9ede4289f0f ! 'm1.ln.w.scale' [0s] Symbol 9b810e76-6ec9-d286-63ca-828dd5f4b3b2
#   'm1.w.proj_in_arr' [3072,768] Array d28bceca4271dd30a4de231c ! 'm1.w.proj_in' [5s,0s] Symbol cd613e30-d8f1-6adf-91b7-584a2265b1f5
#   'm1.w.in_bias_arr' [3072] Array cc12e95bf2f327d278ae92f6 ! 'm1.w.in_bias' [5s] Symbol 1e2feb89-414c-343c-1027-c4d1c386bbc4
#   'm1.w.proj_out_arr' [768,3072] Array 1fbd5d8219a5d212248d9277 ! 'm1.w.proj_out' [0s,5s] Symbol 78e51061-7311-d8a3-c2ce-6f447ed4d57b
#   'm1.w.out_bias_arr' [768] Array 8dded2dcd755340938f78ae9 ! 'm1.w.out_bias' [0s] Symbol 35bf992d-c9e9-c616-612e-7696a6cecc1b
#   'a2.ln.w.bias_arr' [768] Array 09a6f8ea29df20698246fe9a ! 'a2.ln.w.bias' [0s] Symbol 2d3d854e-061b-9030-3b08-c6e33c729578
#   'a2.ln.w.scale_arr' [768] Array 4916ffc15bdde4855028c40e ! 'a2.ln.w.scale' [0s] Symbol 829a48d4-22fe-99a2-2c70-501e533c9135
#   'a2.w.q_arr' [12,64,768] Array 6bef9550b0760ef5592df4c1 ! 'a2.w.q' [4s,7s,0s] Symbol cdbd47d3-64be-8049-a372-db8f6e405d93
#   'a2.w.k_arr' [12,64,768] Array 6b8b996417fb60680e6eef86 ! 'a2.w.k' [4s,7s,0s] Symbol ef8acd12-8b4f-2fc1-5f3f-57ebf30b94fa
#   'a2.w.v_arr' [12,64,768] Array 5986c2f74846096830c8c42e ! 'a2.w.v' [4s,8s,0s] Symbol 5d300cb9-0706-a045-defc-044a09325626
#   'a2.w.o_arr' [12,768,64] Array 4200a1480cd47e42656eea83 ! 'a2.w.o' [4s,0s,8s] Symbol e2520e33-e44c-5055-6c71-c4a66148a86f
#   'a2.w.q_bias_arr' [12,64] Array 332d00ed691712b7e99c6661 ! 'a2.w.q_bias' [4s,7s] Symbol 82523e86-feac-7eb7-dc38-f519b91751da
#   'a2.w.k_bias_arr' [12,64] Array 044bdc2256bebe6041faaed4 ! 'a2.w.k_bias' [4s,7s] Symbol e6b58de7-44ab-6cce-8087-7b6f71e1f6d2
#   'a2.w.v_bias_arr' [12,64] Array 5ca5c8c9cab0bd310d34f8b6 ! 'a2.w.v_bias' [4s,8s] Symbol e8624fab-5186-ee32-ee8d-7ee9770348a0
#   'a2.w.o_bias_arr' [768] Array f2c41d8cbe4e4fda1e458bd3 ! 'a2.w.o_bias' [0s] Symbol 2d6c797f-8f7d-9b78-2a1b-e9cd8697bbd0
#   'm2.ln.w.bias_arr' [768] Array e50bf57c0cbf9c2d350511cb ! 'm2.ln.w.bias' [0s] Symbol 0925e474-9b57-5bd1-3653-f8dd9b1f282e
#   'm2.ln.w.scale_arr' [768] Array 31dbb454b7bd0b59782394dc ! 'm2.ln.w.scale' [0s] Symbol ffed9235-288b-c781-ae66-267594c9c950
#   'm2.w.proj_in_arr' [3072,768] Array c5c62b5e5f38da64c00930d2 ! 'm2.w.proj_in' [5s,0s] Symbol d95bafc8-f2a4-d27b-dcf4-bb99f4bea973
#   'm2.w.in_bias_arr' [3072] Array 38667b94d2de0e788786a1e0 ! 'm2.w.in_bias' [5s] Symbol 5c6e4337-15ba-2bdd-1772-19d30e7a269f
#   'm2.w.proj_out_arr' [768,3072] Array 2015dfdc517da2460ef03a05 ! 'm2.w.proj_out' [0s,5s] Symbol cf1822ff-bc68-8778-2b49-1044d5e34124
#   'm2.w.out_bias_arr' [768] Array 449ad5d2e5b83d72cf60ad56 ! 'm2.w.out_bias' [0s] Symbol 4067c358-4ee2-07f8-da94-e3e8ab73738f
#   'a3.ln.w.bias_arr' [768] Array 0d902e2f4baf9485bd72631e ! 'a3.ln.w.bias' [0s] Symbol 633a50ee-e0f9-e038-eb8f-624fb804d820
#   'a3.ln.w.scale_arr' [768] Array e3cb2a676b919107c714b314 ! 'a3.ln.w.scale' [0s] Symbol 6d4b9adb-ebcd-1f5e-c9c1-8070b6d13089
#   'a3.w.q_arr' [12,64,768] Array ab4f429927c39832a75de072 ! 'a3.w.q' [4s,7s,0s] Symbol 65aa9c82-79f2-48b0-8cb4-a0d7d6225675
#   'a3.w.k_arr' [12,64,768] Array 545764ed653568f1bada31e9 ! 'a3.w.k' [4s,7s,0s] Symbol ed038db4-de38-3784-26d0-b944a2863a7f
#   'a3.w.v_arr' [12,64,768] Array 5a79cba85dde2488a8ed0780 ! 'a3.w.v' [4s,8s,0s] Symbol 28ce6f24-1064-5d51-c6f8-da3eabe19f58
#   'a3.w.o_arr' [12,768,64] Array 9fb045e6dfca161427d0da88 ! 'a3.w.o' [4s,0s,8s] Symbol d2d58443-07f0-62ce-c7b3-17d94d1fe09f
#   'a3.w.q_bias_arr' [12,64] Array 6324f28a458b76c94d2d76ba ! 'a3.w.q_bias' [4s,7s] Symbol 3b5f3d86-268e-cc45-dc6b-f1e1a399f82a
#   'a3.w.k_bias_arr' [12,64] Array 5904b0f9b0373e698461dcbe ! 'a3.w.k_bias' [4s,7s] Symbol 03e0a813-bdc2-ae99-63d2-e49085ef3430
#   'a3.w.v_bias_arr' [12,64] Array 8a9cc8efafb3e5e6fbdc18b2 ! 'a3.w.v_bias' [4s,8s] Symbol 0af438d2-9752-4d6a-f51e-8722c21b6092
#   'a3.w.o_bias_arr' [768] Array a65fb9122213fdaeca21c8a0 ! 'a3.w.o_bias' [0s] Symbol 98418117-7906-1596-44f9-794cdd933160
#   'm3.ln.w.bias_arr' [768] Array ffb966d13a9accd30ff6a50e ! 'm3.ln.w.bias' [0s] Symbol 31162427-3bfd-1d33-8d00-38ec42650644
#   'm3.ln.w.scale_arr' [768] Array ec18b1f325e3f177ec16c16c ! 'm3.ln.w.scale' [0s] Symbol 8a7d43b5-7863-3074-b797-0386fee29476
#   'm3.w.proj_in_arr' [3072,768] Array c5631b41140dc5491c5030a9 ! 'm3.w.proj_in' [5s,0s] Symbol 21636369-8b52-9b4a-97b7-50923ceb3ffd
#   'm3.w.in_bias_arr' [3072] Array 2152a961e570255ea86daf82 ! 'm3.w.in_bias' [5s] Symbol 795b929e-9a9a-80fd-ea7b-5bf55eb561a4
#   'm3.w.proj_out_arr' [768,3072] Array bf8e9fbd21d5a57de0fbb490 ! 'm3.w.proj_out' [0s,5s] Symbol 9b08923d-10c6-7fd9-94b2-b8fda02f34a6
#   'm3.w.out_bias_arr' [768] Array d8f0a48ba7bae0361369b252 ! 'm3.w.out_bias' [0s] Symbol 781f9c58-d664-5fa9-e8a8-529f035efa25
#   'a4.ln.w.bias_arr' [768] Array 7b6ccf9baea480dc5e88d586 ! 'a4.ln.w.bias' [0s] Symbol 3f508249-2d83-a823-3fb6-2d2c81862fc9
#   'a4.ln.w.scale_arr' [768] Array 2859517c8c3897e4ee197bbd ! 'a4.ln.w.scale' [0s] Symbol f1cfd992-16df-6486-47ad-ec26793d0e45
#   'a4.w.q_arr' [12,64,768] Array 28973829120d1dc499e91220 ! 'a4.w.q' [4s,7s,0s] Symbol 43000de0-1b2e-d40e-d3ad-dccb2c33be0a
#   'a4.w.k_arr' [12,64,768] Array e2e8aa8745b2907346301909 ! 'a4.w.k' [4s,7s,0s] Symbol 42a00403-ce80-c4b0-a404-2bb3d4341aad
#   'a4.w.v_arr' [12,64,768] Array c1f23fcf295848fc3a20a5e0 ! 'a4.w.v' [4s,8s,0s] Symbol de08caa1-a081-7910-4a25-e4664f5253a0
#   'a4.w.o_arr' [12,768,64] Array 55fb56d8b48fbfc517576be8 ! 'a4.w.o' [4s,0s,8s] Symbol d8441b56-1633-2aca-5f55-2773e14b0190
#   'a4.w.q_bias_arr' [12,64] Array 2a10d58d68432aded19f3b36 ! 'a4.w.q_bias' [4s,7s] Symbol 06905269-ed6f-0b09-f165-c8ce36e2f24b
#   'a4.w.k_bias_arr' [12,64] Array 603691252d8ab8bfa1a6e2e0 ! 'a4.w.k_bias' [4s,7s] Symbol 2a318785-3184-ff27-4591-42deccea2645
#   'a4.w.v_bias_arr' [12,64] Array 06ed4e6850d16efdf58f7575 ! 'a4.w.v_bias' [4s,8s] Symbol d93936e1-daca-3c06-f5ff-0c03bb5d7385
#   'a4.w.o_bias_arr' [768] Array d182ee6b4f7ed1ca990500f9 ! 'a4.w.o_bias' [0s] Symbol 634f806f-abf4-a07c-5660-02249b191bf4
#   'm4.ln.w.bias_arr' [768] Array f0079d4c446cbc007dd3789c ! 'm4.ln.w.bias' [0s] Symbol 8534f457-38d0-48ec-0f10-99c6c3e1b258
#   'm4.ln.w.scale_arr' [768] Array 77eac218b9722ae4f26ef278 ! 'm4.ln.w.scale' [0s] Symbol c79d6793-46d4-ac7a-5c39-02b38963dc6e
#   'm4.w.proj_in_arr' [3072,768] Array 348547dafe6a52c77189d501 ! 'm4.w.proj_in' [5s,0s] Symbol b8a1abcd-1a69-16c7-4da4-f9fc3c6da5d7
#   'm4.w.in_bias_arr' [3072] Array ff2a3e4409b2459d56218016 ! 'm4.w.in_bias' [5s] Symbol 1710cf53-27ac-435a-7a97-c643656412a9
#   'm4.w.proj_out_arr' [768,3072] Array 26075ee90a389751db5efde9 ! 'm4.w.proj_out' [0s,5s] Symbol 8ca59966-66ce-ab36-0512-bd1311072231
#   'm4.w.out_bias_arr' [768] Array 835944b929354f6f7ea43ff1 ! 'm4.w.out_bias' [0s] Symbol fd724452-ccea-71ff-4a14-876aeaff1a09
#   'a5.ln.w.bias_arr' [768] Array ce1bfc257434f729ef57dd97 ! 'a5.ln.w.bias' [0s] Symbol f5cae3bf-3729-c619-c60a-3cab359eeefb
#   'a5.ln.w.scale_arr' [768] Array 6c4c9644e0da0388788edf89 ! 'a5.ln.w.scale' [0s] Symbol 2a9eba0c-df56-1d80-2a75-9159fb7ff337
#   'a5.w.q_arr' [12,64,768] Array 149e642ff2a536696ddba311 ! 'a5.w.q' [4s,7s,0s] Symbol 617959ce-3f1f-65a8-de52-71007814e8a2
#   'a5.w.k_arr' [12,64,768] Array 6001e89ade20f3a2050e00aa ! 'a5.w.k' [4s,7s,0s] Symbol 687c966c-377b-9aa2-bb2e-db20035b7399
#   'a5.w.v_arr' [12,64,768] Array c5d28eeab4a0a80be5023967 ! 'a5.w.v' [4s,8s,0s] Symbol c30d8b76-28db-d25e-63b2-29f1c4069545
#   'a5.w.o_arr' [12,768,64] Array c3b754d87d710ca1e42b455c ! 'a5.w.o' [4s,0s,8s] Symbol 21da8978-206f-5c66-71e0-c07e9e115e4b
#   'a5.w.q_bias_arr' [12,64] Array 0ae54031f880a9eac0c17eb0 ! 'a5.w.q_bias' [4s,7s] Symbol 3fd42359-92ed-cf45-1a1a-fe878b33e968
#   'a5.w.k_bias_arr' [12,64] Array 2f0167777ca8ab80fd464b67 ! 'a5.w.k_bias' [4s,7s] Symbol de11cc9d-ea95-9c21-2e9c-82b1478c281d
#   'a5.w.v_bias_arr' [12,64] Array 7777d94ba6517daa3b5fa726 ! 'a5.w.v_bias' [4s,8s] Symbol 9e30691c-2386-42ea-126a-1e48cc11d357
#   'a5.w.o_bias_arr' [768] Array b7b0216c848a60f4a44f4153 ! 'a5.w.o_bias' [0s] Symbol 015c33b2-df14-61aa-f8eb-18b900745130
#   'm5.ln.w.bias_arr' [768] Array 7acc8d333ab8c75be75be5a4 ! 'm5.ln.w.bias' [0s] Symbol 0d464138-a623-3255-3fc1-ea36f17fd374
#   'm5.ln.w.scale_arr' [768] Array f8be135a601d087ea26711c2 ! 'm5.ln.w.scale' [0s] Symbol 5f2dd97f-1cfb-10f6-2827-688de6a16a3b
#   'm5.w.proj_in_arr' [3072,768] Array be1a55e778cb20257bf2871c ! 'm5.w.proj_in' [5s,0s] Symbol 5bc8fbbc-bde5-c099-4164-d8399f767c45
#   'm5.w.in_bias_arr' [3072] Array 2b0df5eb66996e8b36613254 ! 'm5.w.in_bias' [5s] Symbol d76d4330-f144-6bea-b0c1-1fdecb91ce37
#   'm5.w.proj_out_arr' [768,3072] Array d64410fe31249e6bb545b4a4 ! 'm5.w.proj_out' [0s,5s] Symbol 87b0b125-ec1d-7da0-a6eb-8c9ebd69fe29
#   'm5.w.out_bias_arr' [768] Array 1b6463a649b155cc070f6f74 ! 'm5.w.out_bias' [0s] Symbol c6a53877-7733-0bdb-d721-0dff076ce2ef
#   'a6.ln.w.bias_arr' [768] Array e299e86fbcfe93a6f730c296 ! 'a6.ln.w.bias' [0s] Symbol b3642b19-3279-3637-c16c-f5c51801fd9a
#   'a6.ln.w.scale_arr' [768] Array b2da920807ab8590086edebc ! 'a6.ln.w.scale' [0s] Symbol 18f918e2-4a8b-0188-cbe1-9514a28a0aaa
#   'a6.w.q_arr' [12,64,768] Array 31b41bbae8bda7902425476d ! 'a6.w.q' [4s,7s,0s] Symbol e91b4ad1-69fc-5360-df5c-a32ebad5ccc2
#   'a6.w.k_arr' [12,64,768] Array 57bff1be9df75666cdc14fea ! 'a6.w.k' [4s,7s,0s] Symbol b313fc7e-8db9-b92c-903c-2ac9316774fe
#   'a6.w.v_arr' [12,64,768] Array 9be3c843255be4658b73f11f ! 'a6.w.v' [4s,8s,0s] Symbol 168e5087-af89-5f5b-9c2c-0ac2cda95957
#   'a6.w.o_arr' [12,768,64] Array de48565aabc20b14f30a3a54 ! 'a6.w.o' [4s,0s,8s] Symbol 68f22599-ccdf-540b-5cb5-3ec017d7ab26
#   'a6.w.q_bias_arr' [12,64] Array faef4ab9cf92370da98061ae ! 'a6.w.q_bias' [4s,7s] Symbol 181e290a-ae9a-f169-8a0c-510089ce5ef7
#   'a6.w.k_bias_arr' [12,64] Array d18d97d594fff8cff21d4250 ! 'a6.w.k_bias' [4s,7s] Symbol a9b3d1a2-43f9-300c-ba98-666ace1c9c17
#   'a6.w.v_bias_arr' [12,64] Array 5033e036e1268879e459c0a3 ! 'a6.w.v_bias' [4s,8s] Symbol fd802060-55e8-b3eb-6cb9-185ed822e2f9
#   'a6.w.o_bias_arr' [768] Array 6b8673e6be3d803c85c0bb2f ! 'a6.w.o_bias' [0s] Symbol b31a5bf3-71f9-70cf-401f-e4fcce06294d
#   'm6.ln.w.bias_arr' [768] Array f40f03605390f6c910fa8681 ! 'm6.ln.w.bias' [0s] Symbol 059a91e1-c527-e279-51c3-42505f877031
#   'm6.ln.w.scale_arr' [768] Array aef80a118bc687dd66057325 ! 'm6.ln.w.scale' [0s] Symbol 32b7228f-cd4a-5557-7d24-b39645cf8aa4
#   'm6.w.proj_in_arr' [3072,768] Array fe2b91126965219baa39be86 ! 'm6.w.proj_in' [5s,0s] Symbol 14a03569-d26b-9496-92e5-dfe8cb1855fe
#   'm6.w.in_bias_arr' [3072] Array 47aab50b3e6af44b206a4f3b ! 'm6.w.in_bias' [5s] Symbol 096d3737-42f9-a039-c320-a4737c2b3abe
#   'm6.w.proj_out_arr' [768,3072] Array 5fcb338ac94cf64cbf8102b4 ! 'm6.w.proj_out' [0s,5s] Symbol 9623d7cf-a9ae-7a34-2544-99c7001d9a88
#   'm6.w.out_bias_arr' [768] Array 5504f5ec7d1814acfdfc1525 ! 'm6.w.out_bias' [0s] Symbol bc1e3ac1-c27d-b4ec-f72c-2c2678629522
#   'a7.ln.w.bias_arr' [768] Array a8bc414d96490a6f79f9d333 ! 'a7.ln.w.bias' [0s] Symbol 923a7369-94e3-bf91-1a61-dbe22e44158b
#   'a7.ln.w.scale_arr' [768] Array 4b19ef0ad24c89b721adedcd ! 'a7.ln.w.scale' [0s] Symbol 18f135d2-5f55-7203-3018-50c5a38fd547
#   'a7.w.q_arr' [12,64,768] Array f2731beb1a4f1d51efb14fcc ! 'a7.w.q' [4s,7s,0s] Symbol 90c192cf-d3ac-94af-0f21-ddb66cad4a26
#   'a7.w.k_arr' [12,64,768] Array 912872639c6f384d4c26469b ! 'a7.w.k' [4s,7s,0s] Symbol 0fd630f1-f29d-0da9-953f-48f1a09f76b5
#   'a7.w.v_arr' [12,64,768] Array f7cadc0ee191432d7474ee5b ! 'a7.w.v' [4s,8s,0s] Symbol 8e81973e-0bec-d7b0-3898-d190f9ebdacc
#   'a7.w.o_arr' [12,768,64] Array 621079f1fecb8c37091ec7db ! 'a7.w.o' [4s,0s,8s] Symbol 92276658-1e27-a1c0-8a6a-63ec24ede6a4
#   'a7.w.q_bias_arr' [12,64] Array 8705718924f1e3a56a9825b8 ! 'a7.w.q_bias' [4s,7s] Symbol a170b338-3926-3059-f28c-105d1fb17c23
#   'a7.w.k_bias_arr' [12,64] Array b03aa64dde9523701323bb0a ! 'a7.w.k_bias' [4s,7s] Symbol 0cb1e29c-658c-da14-95e6-0af593bd04cf
#   'a7.w.v_bias_arr' [12,64] Array dbda3f4bd47a592d4b3b3a5a ! 'a7.w.v_bias' [4s,8s] Symbol 6b4cb242-4a23-d596-2217-beaddbc496cb
#   'a7.w.o_bias_arr' [768] Array 1205d32607eb94acc9f58f79 ! 'a7.w.o_bias' [0s] Symbol ae97ba94-d0ed-a82f-8f6d-05584ef8aa38
#   'm7.ln.w.bias_arr' [768] Array 55067071af4948b68b65b794 ! 'm7.ln.w.bias' [0s] Symbol 6b0d549b-6f03-675a-1600-a35a099950d8
#   'm7.ln.w.scale_arr' [768] Array 91f4297e51165c716211dfe2 ! 'm7.ln.w.scale' [0s] Symbol 8d116ece-1738-f7d9-3d9c-172411e20b8f
#   'm7.w.proj_in_arr' [3072,768] Array 37cf189e7b7b24371041a474 ! 'm7.w.proj_in' [5s,0s] Symbol 6513270e-269e-0d37-f2a7-4de452e6b438
#   'm7.w.in_bias_arr' [3072] Array 785b0f7b3bceca6091780cac ! 'm7.w.in_bias' [5s] Symbol d23f0824-128b-2f33-0c5c-7fd0a6a3a450
#   'm7.w.proj_out_arr' [768,3072] Array dca283786ec766a460bf5712 ! 'm7.w.proj_out' [0s,5s] Symbol 9531985d-5d9d-c9f8-1818-e811892f902b
#   'm7.w.out_bias_arr' [768] Array f5f20d6effdb5941c6dc9214 ! 'm7.w.out_bias' [0s] Symbol 36f675cc-81e7-4ef5-e8e2-5d940ed90475
#   'a8.ln.w.bias_arr' [768] Array b6de5bf0e215bdf5efffc2c6 ! 'a8.ln.w.bias' [0s] Symbol 1607b1c4-b0f9-1306-3c02-e56756a3e957
#   'a8.ln.w.scale_arr' [768] Array aa478f6a0a43f451bf83f4a3 ! 'a8.ln.w.scale' [0s] Symbol 844dbc0c-a654-23a9-e744-b24e7f61701e
#   'a8.w.q_arr' [12,64,768] Array 4d61af1f9a5d7fc6e9f01f01 ! 'a8.w.q' [4s,7s,0s] Symbol 67164890-d49d-0ac1-e5b8-063831360a40
#   'a8.w.k_arr' [12,64,768] Array f58a6eaaf74077af93d5516f ! 'a8.w.k' [4s,7s,0s] Symbol 852a5fba-444a-df42-b37f-5722051e2670
#   'a8.w.v_arr' [12,64,768] Array 95a0f431dbb3911151e4cde7 ! 'a8.w.v' [4s,8s,0s] Symbol a9b7e3ea-1d1d-784f-b9db-434b610b1631
#   'a8.w.o_arr' [12,768,64] Array 69a4f0c561b50c159efe21f5 ! 'a8.w.o' [4s,0s,8s] Symbol d45c39a3-9ec3-53c1-62e9-17d310269470
#   'a8.w.q_bias_arr' [12,64] Array dc1e6a8bd49b8cfa86716676 ! 'a8.w.q_bias' [4s,7s] Symbol c24f6aa8-3bf3-6a14-7c2f-7ad016edc5d4
#   'a8.w.k_bias_arr' [12,64] Array 2446c2072045ee89c79c3ac9 ! 'a8.w.k_bias' [4s,7s] Symbol e941aa79-e6ed-af80-796d-3bc4685ca8af
#   'a8.w.v_bias_arr' [12,64] Array b13a3c4410d068d3d1b36ca7 ! 'a8.w.v_bias' [4s,8s] Symbol d0718c1a-fdd9-a78d-18df-f3934223aa56
#   'a8.w.o_bias_arr' [768] Array 4721668a7c2023ebcb814020 ! 'a8.w.o_bias' [0s] Symbol 0edca4ec-a92d-04a3-1b94-1f4360908405
#   'm8.ln.w.bias_arr' [768] Array 79cfcee256b66fad26ecd2ae ! 'm8.ln.w.bias' [0s] Symbol 7cc661e9-7589-ca4a-07c1-5471a4517d6c
#   'm8.ln.w.scale_arr' [768] Array 43b9f1936fe05a6e23d3465e ! 'm8.ln.w.scale' [0s] Symbol 92b850ad-7eb7-2f82-63f6-5da874007cb4
#   'm8.w.proj_in_arr' [3072,768] Array d605100a49084a8a18f57a97 ! 'm8.w.proj_in' [5s,0s] Symbol 6018366c-f658-f7a7-5ed3-4fe53a096533
#   'm8.w.in_bias_arr' [3072] Array 59c5e42508639af57fb58f8a ! 'm8.w.in_bias' [5s] Symbol 0b3510b0-b46e-e1da-3170-17a6205738d1
#   'm8.w.proj_out_arr' [768,3072] Array 598e4a2dbf40234543b028bf ! 'm8.w.proj_out' [0s,5s] Symbol cfaf0010-3f58-4ad4-2308-24d215ceb3a1
#   'm8.w.out_bias_arr' [768] Array 8cef5a8a889c3c7bccdedfbf ! 'm8.w.out_bias' [0s] Symbol 6694f229-359b-1548-81a0-d5b3ffc6e35c
#   'a9.ln.w.bias_arr' [768] Array 26c4b5d0911ebe27531ad2aa ! 'a9.ln.w.bias' [0s] Symbol c5c7d186-1674-518d-e3bb-41b36bf82959
#   'a9.ln.w.scale_arr' [768] Array 2d757f5523248058d3729e2e ! 'a9.ln.w.scale' [0s] Symbol 6583d614-35bb-5c11-e950-27004448a6a1
#   'a9.w.q_arr' [12,64,768] Array 749e3921ccf4a9eb24cf5025 ! 'a9.w.q' [4s,7s,0s] Symbol f3868254-73b7-a490-f23b-2cc4b4174a67
#   'a9.w.k_arr' [12,64,768] Array 2eecd09c53f66cbfee410f15 ! 'a9.w.k' [4s,7s,0s] Symbol 21e6a46f-1c67-0ea9-0d24-3a163cee5e2c
#   'a9.w.v_arr' [12,64,768] Array 34833bf962d86848248ea9bc ! 'a9.w.v' [4s,8s,0s] Symbol b03da701-c632-976a-1036-3c5f972651da
#   'a9.w.o_arr' [12,768,64] Array 5cc649a06844f7b26b01c8b8 ! 'a9.w.o' [4s,0s,8s] Symbol 3478442b-4a8a-a593-eb40-a9b81a070205
#   'a9.w.q_bias_arr' [12,64] Array 6c59a5a299a7f49872daa908 ! 'a9.w.q_bias' [4s,7s] Symbol 2b1e1885-283b-73a6-6c2e-a417b99de255
#   'a9.w.k_bias_arr' [12,64] Array c0d48503c6c4a7ae36187369 ! 'a9.w.k_bias' [4s,7s] Symbol fdb119a9-ec80-1bdf-df29-65b3819ad93b
#   'a9.w.v_bias_arr' [12,64] Array a54960ff07ecbf64388bea51 ! 'a9.w.v_bias' [4s,8s] Symbol e323bb2a-bf00-188d-ca22-e4c76237dbe6
#   'a9.w.o_bias_arr' [768] Array b14a34e2b297c78ec57ef0c9 ! 'a9.w.o_bias' [0s] Symbol cb01c357-b9c7-e435-396b-cb8fac9abb0c
#   'm9.ln.w.bias_arr' [768] Array 3b33846598253ad0f7379d90 ! 'm9.ln.w.bias' [0s] Symbol b339a476-9ddc-c6f8-efb6-fbfe8de4ab47
#   'm9.ln.w.scale_arr' [768] Array 74085c06622d359f30674894 ! 'm9.ln.w.scale' [0s] Symbol 2b5ebaa0-6107-6dc3-ba6a-ce6c0a78250f
#   'm9.w.proj_in_arr' [3072,768] Array 1e02ff436776676edcd4c6a8 ! 'm9.w.proj_in' [5s,0s] Symbol 4462ebfc-5f91-5ef0-9cfb-ac6e7687a66e
#   'm9.w.in_bias_arr' [3072] Array 368584834a25da3851f88775 ! 'm9.w.in_bias' [5s] Symbol ad38835e-ddd6-ff55-2fa7-3207237751aa
#   'm9.w.proj_out_arr' [768,3072] Array 6d81000d8018038ce5e4d783 ! 'm9.w.proj_out' [0s,5s] Symbol 76b67451-80b6-5386-569c-803601a5ba50
#   'm9.w.out_bias_arr' [768] Array 3b6757c0ac358a359a0a5d38 ! 'm9.w.out_bias' [0s] Symbol 558298e2-14b0-44d7-9acd-8acde5f6db1d
#   'a10.ln.w.bias_arr' [768] Array 204fe3b2ac0b8aa6c9f3c4cf ! 'a10.ln.w.bias' [0s] Symbol 31e875ba-224c-0601-3c53-d0e30109c207
#   'a10.ln.w.scale_arr' [768] Array e9582b344eb52610b42bb6e4 ! 'a10.ln.w.scale' [0s] Symbol 894deab4-4d88-450f-e8da-c663f0e58650
#   'a10.w.q_arr' [12,64,768] Array 26aa0a91dd167a3053f12d12 ! 'a10.w.q' [4s,7s,0s] Symbol 6b9f15c4-0b68-0c1c-5c74-e45eff1e5bef
#   'a10.w.k_arr' [12,64,768] Array 45618735b57ee6af6420abb8 ! 'a10.w.k' [4s,7s,0s] Symbol d3ac535f-489b-340f-6bd7-f50361b0ee09
#   'a10.w.v_arr' [12,64,768] Array a54ca681d6189ce0b4b64c3f ! 'a10.w.v' [4s,8s,0s] Symbol 5cd2875e-a96e-c2b3-4d98-4bffaf949e5e
#   'a10.w.o_arr' [12,768,64] Array 0f6fdeaf0051cd3aa07e5fd9 ! 'a10.w.o' [4s,0s,8s] Symbol 708cc1b6-f829-d29f-3d48-06c2fb7f6f5d
#   'a10.w.q_bias_arr' [12,64] Array 33898cfe3d6fc8caed150352 ! 'a10.w.q_bias' [4s,7s] Symbol 5ae6a228-9a6a-b329-2381-23e5dc338383
#   'a10.w.k_bias_arr' [12,64] Array 3ea0abb517cb257431b3e19c ! 'a10.w.k_bias' [4s,7s] Symbol 2cb7362c-74f2-e2ed-4327-79eeacca7f0d
#   'a10.w.v_bias_arr' [12,64] Array ed49ed1463e07e0ef76d921b ! 'a10.w.v_bias' [4s,8s] Symbol dc2c2e2c-c491-04d0-74f9-42cb220adb0a
#   'a10.w.o_bias_arr' [768] Array 587315312c11c6c605064b66 ! 'a10.w.o_bias' [0s] Symbol 953b00b0-0b54-aa22-600f-ecc19d02fc90
#   'm10.ln.w.bias_arr' [768] Array 4f224167100c81e818abe9a6 ! 'm10.ln.w.bias' [0s] Symbol 137a9777-53e8-eb43-7d76-3fb9854a9657
#   'm10.ln.w.scale_arr' [768] Array cd9d0cc126c56bd63f063934 ! 'm10.ln.w.scale' [0s] Symbol bedc25e6-f3eb-cf12-f3d0-6f863fffc830
#   'm10.w.proj_in_arr' [3072,768] Array 3af123dcc5d43cded8ba06a6 ! 'm10.w.proj_in' [5s,0s] Symbol 7b89296c-6dcb-ac50-0857-7eb1924770d3
#   'm10.w.in_bias_arr' [3072] Array ef44bb7ea62544a1454e4239 ! 'm10.w.in_bias' [5s] Symbol 766bad07-34c2-da80-03cc-0f2793fdcab8
#   'm10.w.proj_out_arr' [768,3072] Array 471ca6d3aab1d42bfc11fdc8 ! 'm10.w.proj_out' [0s,5s] Symbol 470b9805-d2d6-b877-7dc5-9a3ad035d259
#   'm10.w.out_bias_arr' [768] Array 5a0ba6291353be100550a8d7 ! 'm10.w.out_bias' [0s] Symbol 08ceac39-2904-cdef-cf84-b683a749f9c5
#   'a11.ln.w.bias_arr' [768] Array 0354348a5e5e76080c298fee ! 'a11.ln.w.bias' [0s] Symbol 320094ea-d7a9-4ded-9749-1e2370c6a5b8
#   'a11.ln.w.scale_arr' [768] Array 311eaac357f33fd1f57ae594 ! 'a11.ln.w.scale' [0s] Symbol 4b4d8474-a3ea-284d-3bd0-334684e55160
#   'a11.w.q_arr' [12,64,768] Array 27b8a5a29fdf846be6358ae5 ! 'a11.w.q' [4s,7s,0s] Symbol e3eff9c0-cf44-dd3f-89e7-d15f17362f25
#   'a11.w.k_arr' [12,64,768] Array d464ae8b3a20f746fbebb47e ! 'a11.w.k' [4s,7s,0s] Symbol 73f778aa-f6fa-5db8-656a-bd72fb710734
#   'a11.w.v_arr' [12,64,768] Array d569195b7e32ff26c65486b8 ! 'a11.w.v' [4s,8s,0s] Symbol d4ea65d0-03d7-1684-9f85-58a628518867
#   'a11.w.o_arr' [12,768,64] Array f9d9b15d185e03baf2252c5e ! 'a11.w.o' [4s,0s,8s] Symbol 99809225-3def-fa38-e12b-2b8f30b17d0b
#   'a11.w.q_bias_arr' [12,64] Array 69fe0e7784ec280b89e1f99c ! 'a11.w.q_bias' [4s,7s] Symbol 986e86cb-0ab8-ab67-a26b-7f62b1852f27
#   'a11.w.k_bias_arr' [12,64] Array 3357eb518d0775e73fdf2ec7 ! 'a11.w.k_bias' [4s,7s] Symbol a66b0d38-9d95-847e-bd29-9753a7677796
#   'a11.w.v_bias_arr' [12,64] Array c2a1a38e831a6c1120e00ca1 ! 'a11.w.v_bias' [4s,8s] Symbol 09208a65-0f3e-bdd3-102b-938b8743feb6
#   'a11.w.o_bias_arr' [768] Array f77dfbaf3d05a1857db87e9f ! 'a11.w.o_bias' [0s] Symbol 5387f613-76c4-68ae-c732-1cc007b37e14
#   'm11.ln.w.bias_arr' [768] Array 36eeea068893621f7c3f0660 ! 'm11.ln.w.bias' [0s] Symbol 2fa91425-cb00-8853-9d2c-67eda13ffe79
#   'm11.ln.w.scale_arr' [768] Array 6fc0cab3f8360125b859ec21 ! 'm11.ln.w.scale' [0s] Symbol 244caf9c-4dab-b481-7253-edc618187993
#   'm11.w.proj_in_arr' [3072,768] Array 3abb8fbb5fee4c667aa80af8 ! 'm11.w.proj_in' [5s,0s] Symbol db5b5fab-8f4d-3e27-dda1-494c73cf256d
#   'm11.w.in_bias_arr' [3072] Array 2c164f2e48f91e3ced0c7ab0 ! 'm11.w.in_bias' [5s] Symbol 73ab4876-7734-d7c1-c7fd-e805ec99108d
#   'm11.w.proj_out_arr' [768,3072] Array a729aa0277a2f6ecc729843d ! 'm11.w.proj_out' [0s,5s] Symbol 309d6b79-965e-da32-dae4-45508201e2bd
#   'm11.w.out_bias_arr' [768] Array 29c898d490237f73d915e15e ! 'm11.w.out_bias' [0s] Symbol 79cb9e86-830c-71c2-cdcc-69292f45e678
#   'final.ln.w.bias_arr' [768] Array a6f0ac1de32ab667e10fcd1d ! 'final.ln.w.bias'
#   'final.ln.w.scale_arr' [768] Array ea8915931fdea0d8e8f39b20 ! 'final.ln.w.scale'
#   't.w.unembed_arr' [50257,768] Array 1f668798fb95d0e16b2a0143 ! 't.w.unembed'

# # originally gelu_twelve_layers (aka gpt2-small)
# # also called gelu_12_tied.circ"""