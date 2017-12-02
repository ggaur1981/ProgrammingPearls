read -a array
sum=0
for i in ${array[@]}; do
    sum=$(expr $sum + $i)    
done
echo "Sum: $sum"