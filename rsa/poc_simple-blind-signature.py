# RSA setup
e=13
d=37
p,q=7,11
n,phin=p*q,(p-1)*(q-1)

# message
m=42

# r for blind signature
r=9  # gcd(9,77)=1
r_inv = 60  # r*r_inv mod 77 = 1

# prepare message for signer
m_ = m*r**e % n

# blind signing by signer
s_ = m_**d % n

# get actual signature
s = s_*r_inv % n

print("Message: %s (%s for signer)" % (m, m_))
print("Signature: %s (%s for signer)" % (s, s_))

# verify
v = s**e % n
v_ = s_**e % n
print("Verification: %s == %s ?" % (v, m))
print("Verification for signer: %s == %s ?" % (v_, m_))

