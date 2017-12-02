read -a array
sum=0
for i in ${array[@]}; do
  let sum+=$i
done
echo "Sum: $sum"